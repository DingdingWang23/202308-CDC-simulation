import os
import argparse
from functools import partial

import paddle
from data import convert_example, create_dataloader, read_text_pair

from paddlenlp.data import Pad, Tuple
from paddlenlp.datasets import load_dataset
from paddlenlp.transformers import AutoModel, AutoTokenizer

import openpyxl

# fmt: off
parser = argparse.ArgumentParser()
# parser.add_argument("--input_file", type=str, required=True, help="The full path of input file")
# parser.add_argument("--params_path", type=str, required=True, help="The path to model parameters to be loaded.")
parser.add_argument("--max_seq_length", default=1024, type=int,
                    help="The maximum total input sequence length after tokenization. Sequences longer than this will be truncated, sequences shorter will be padded.")
parser.add_argument("--batch_size", default=2048, type=int, help="Batch size per GPU/CPU for training.")
parser.add_argument('--device', choices=['cpu', 'gpu'], default="cpu",
                    help="Select which device to train model, defaults to cpu.")
args = parser.parse_args()


# fmt: on


def predict(model, data_loader):
    """
    Predicts the similarity.

    Args:
        model (obj:`SemanticIndexBase`): A model to extract text embedding or calculate similarity of text pair.
        data_loader (obj:`List(Example)`): The processed data ids of text pair: [query_input_ids, query_token_type_ids, title_input_ids, title_token_type_ids]
    Returns:
        results(obj:`List`): cosine similarity of text pairs.
    """
    results = []

    model.eval()

    with paddle.no_grad():
        # print('DEF')
        for batch_data in data_loader:
            # print('EFG')
            query_input_ids, query_token_type_ids, title_input_ids, title_token_type_ids = batch_data
            query_input_ids = paddle.to_tensor(query_input_ids)
            query_token_type_ids = paddle.to_tensor(query_token_type_ids)
            title_input_ids = paddle.to_tensor(title_input_ids)
            title_token_type_ids = paddle.to_tensor(title_token_type_ids)

            vecs_query = model(input_ids=query_input_ids, token_type_ids=query_token_type_ids)
            vecs_title = model(input_ids=title_input_ids, token_type_ids=title_token_type_ids)
            vecs_query = vecs_query[1].numpy()
            vecs_title = vecs_title[1].numpy()

            vecs_query = vecs_query / (vecs_query ** 2).sum(axis=1, keepdims=True) ** 0.5
            vecs_title = vecs_title / (vecs_title ** 2).sum(axis=1, keepdims=True) ** 0.5
            sims = (vecs_query * vecs_title).sum(axis=1)

            results.extend(sims)

            print("sims=", sims)
            break
        print("A:results=", results)
    print("B:results=", results)

    return results


def excel_to_dict(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    data_dict = {}
    for row in sheet.iter_rows(values_only=True):
        if row[0] == "匹配名称":  # 根据实际情况替换为标题列的列名
            continue  # 跳过标题行
        key = row[0]
        value = row[1]
        data_dict[key] = value

    return data_dict


if __name__ == "__main__":
    paddle.set_device(args.device)

    model = AutoModel.from_pretrained("simbert-base-chinese", pool_act="linear")
    tokenizer = AutoTokenizer.from_pretrained("simbert-base-chinese")

    trans_func = partial(convert_example, tokenizer=tokenizer, max_seq_length=args.max_seq_length, phase="predict")

    batchify_fn = lambda samples, fn=Tuple(
        Pad(axis=0, pad_val=tokenizer.pad_token_id),  # query_input
        Pad(axis=0, pad_val=tokenizer.pad_token_type_id),  # query_segment
        Pad(axis=0, pad_val=tokenizer.pad_token_id),  # title_input
        Pad(axis=0, pad_val=tokenizer.pad_token_type_id),  # title_segment
    ): [data for data in fn(samples)]

    input_folder = r"C:\Users\丁丁\Desktop\上海住建测评\all_sentence_output"
    output_folder = r"C:\Users\丁丁\Desktop\上海住建测评\node_output"

    # 获取输入文件夹中的文件列表
    file_list = os.listdir(input_folder)

    for file_name in file_list:
        if file_name.endswith(".tsv"):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)

            # 读取数据
            valid_ds = load_dataset(read_text_pair, data_path=input_path, lazy=False)

            valid_data_loader = create_dataloader(
                valid_ds, mode="predict", batch_size=args.batch_size, batchify_fn=batchify_fn, trans_fn=trans_func
            )
            y_sims = predict(model, valid_data_loader)
            print(y_sims)
            valid_ds = load_dataset(read_text_pair, data_path=input_path, lazy=False)

            total_data = []
            for idx, prob in enumerate(y_sims):
                text_pair = valid_ds[idx]
                text_pair["similarity"] = y_sims[idx]
                print(text_pair)
                total_data.append(text_pair)

            result = {}
            print("total_data", total_data)

            for item in total_data:
                query = item['query']
                title = item['title']
                id = item['id']
                similarity = item['similarity']

                if query not in result or similarity > result[query]['similarity']:
                    result[query] = {'id': id, 'title': title, 'similarity': similarity}
                    # result[query] = {'title': title, 'similarity': similarity}

            print(result)

            file_path = r'C:\\Users\\丁丁\\Desktop\\mapping_1110.xlsx'
            excel_dict = excel_to_dict(file_path)

            '''
            file = open(output_path, 'w+', encoding="utf-8")

            result_keys = []
            for data in total_data:
                result_keys.append(data['query'])

            result_keys = result_keys[::10]

            print(result_keys)

            title_list = []
            id_list = []
            similarity_list = []

            for result_key in result_keys:
                title_list.append(result[result_key]['title'])
                id_list.append(result[result_key]['id'])
                similarity_list.append(result[result_key]['similarity'])
            print(title_list)
            print(id_list)
            print(similarity_list)
            mapping_list = []
            for title in title_list:
                mapping_list.append(excel_dict[title.strip()])

            for i, key in enumerate(title_list):
                if (i < len(title_list) - 1) and (i % 2 == 0) and similarity_list[i] > 0.35 and similarity_list[i + 1] > 0.35:
                    print(id_list[i], mapping_list[i], id_list[i + 1], mapping_list[i + 1], file=file)

            file.close()

            '''

            file = open(output_path, 'w+', encoding="utf-8")

            for query in result.keys():
                if result[query]['similarity'] > 0.4:
                    output = excel_dict[result[query]['title'].strip()]
                    print(result[query]['id'], output, file=file)

            file.close()





