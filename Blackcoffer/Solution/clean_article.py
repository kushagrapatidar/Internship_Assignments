from txt_reader import read_txt_folder
from re import sub
import string

def clean_stopwords(stopwords_txt):
    cleaned_stopwords=[]
    for txt in stopwords_txt:
        cleaned_stopwords+=txt.lower().split('\n')
    length_stopwords = len(cleaned_stopwords)
    for i in range(length_stopwords):
        if ' |' in cleaned_stopwords[i]:
            cleaned_stopwords[i]=cleaned_stopwords[i].split('|')[0]
        cleaned_stopwords[i]=cleaned_stopwords[i].strip()
    return cleaned_stopwords

def remove_stopwords(article_content):
    stopwords_txt=read_txt_folder("StopWords/")
    stopwords_lst=clean_stopwords(stopwords_txt)
    punctuations = string.punctuation
    punctuations=punctuations.replace('.','')
    for _ in punctuations:
            article_content = article_content.replace(_, " ")
    article_content=article_content.replace("'s", "")
    article_content=article_content.replace("s'", "")
    article_content = sub(r' \d+', '', article_content)
    for stopword in stopwords_lst:
        if stopword in article_content:
            article_content = sub(r' '+stopword+'\s', ' ', article_content)
            article_content = sub(r'\s+', ' ', article_content)
    
    return article_content