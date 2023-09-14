from txt_reader import read_txt_folder

def get_masterdict():
    fdr_path="MasterDictionary/"
    master_dict=read_txt_folder(fdr_path)
    for _ in range(len(master_dict)):
        master_dict[_]=master_dict[_].split('\n')
    return master_dict

def annote_txt(text):
    positive=0
    negative=0
    master_dict=get_masterdict()
    for word in text:
        if word in master_dict[0]:
            negative-=1
        elif word in master_dict[1]:
            positive+=1
    return positive,negative
