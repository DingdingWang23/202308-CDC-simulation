import os
import re
from docx import Document

'''
def read_docx(file_path):
    doc = Document(file_path)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return '\n'.join(text)
'''
def read_txt(file_path):
    with open(file_path,"r") as f:
        content = f.read()
    return content

def split_text(text, chunk_size=1000):
    chunks = []
    i = 0
    while i < len(text):
        chunks.append(text[i:i + chunk_size])
        i += chunk_size
    return chunks


def save_to_txt(chunks, folder_path,file_name):
    count = 1
    for i, chunk in enumerate(chunks):
        with open(folder_path+f"{file_name}_{count}.txt", 'w', encoding='utf-8') as f:
            f.write(chunk + '\n\n')
        count += 1
        print(count)


def process_folder(folder_path):
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    print(txt_files)
    for docx_file in txt_files:
        text = read_txt(os.path.join(folder_path, docx_file))
        print(text)
        chunks = split_text(text)
        print(chunks)
        save_to_txt(chunks, folder_path,docx_file[:-4])

folder_path = r"C://Users//丁丁//Desktop//物资集团测评//每个人讲的话//"
process_folder(folder_path)