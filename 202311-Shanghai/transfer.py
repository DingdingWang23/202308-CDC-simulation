import os

input_folder = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\group_id_node_output"
output_folder = r"C:\\Users\\丁丁\\Desktop\\物资集团测评\\1130\\group 5\\for_reasoning"

for filename in os.listdir(input_folder):

    if filename.endswith('.tsv'):
        input_filepath = os.path.join(input_folder, filename)
        output_filepath = os.path.join(output_folder, filename)

        with open(input_filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()

        with open(output_filepath, "w", encoding="utf-8", newline="") as file:
            for i, line in enumerate(lines):
                id = i//5+1
                file.write(f"{id}  {line.strip()}\n")