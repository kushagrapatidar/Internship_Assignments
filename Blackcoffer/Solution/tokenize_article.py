from nltk.tokenize import word_tokenize, sent_tokenize

def article_tokens(article_content):
    sentences = sent_tokenize(article_content)
    
    for _ in range(len(sentences)):
        sentences[_] = sentences[_].rstrip('.')
        sentences[_] = sentences[_].rstrip()
    words = []
    
    for sentence in sentences:
        words += word_tokenize(sentence)
        
    return sentences,words