import os

def read_txt(url_id):
    # Output filename
    file_path = 'Articles/'+url_id+'.txt'

    # Open the file in write mode ('w')
    with open(file_path, 'r', encoding='utf-8') as file:
        text=file.read()
    return text

def read_txt_folder(fdr_path):
    text_files = [f for f in os.listdir(fdr_path) if f.endswith(".txt")]
    texts=[]
    for file_name in text_files:
        file_path = os.path.join(fdr_path, file_name)

        # Open the file in read mode
        with open(file_path, 'r') as file:
            texts.append(file.read())
            
    return texts