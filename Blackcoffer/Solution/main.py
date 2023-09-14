from xl_reader import get_urls
from txt_reader import read_txt
from clean_article import remove_stopwords
from tokenize_article import article_tokens
from calc_derivedvar import calc_scores
from complex_words import find_complex
from personal_pronouns import count_personal_pronouns
from xl_saver import save_data,reformat


fpath="input.xlsx"
ofpath='analysis_outputs.xlsx'
#Run the extractor.py program once before executing this code
#as it extracts and saves the content to txt file for analysis

#Get URL dictionary
urls=get_urls(fpath)
key_lst = ['URL_ID', 'URL', 'POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 'SUBJECTIVITY SCORE', 'AVG SENTENCE LENGTH', 'PERCENTAGE OF COMPLEX WORDS',
           'FOG INDEX', 'AVG NUMBER OF WORDS PER SENTENCE', 'COMPLEX WORD COUNT', 'WORD COUNT', 'SYLLABLE PER WORD', 'PERSONAL PRONOUNS', 'AVG WORD LENGTH']
analyzed_urls = {key: list() for key in key_lst}

for url_id in urls.keys():
    url=urls[url_id]
    # Read the saved article content
    article_content=read_txt(url_id).lower()
    if article_content =="page not found | blackcoffer insights\n":
        analyzed_urls['URL_ID'].append(url_id)
        analyzed_urls['URL'].append(url)
        for col in list(analyzed_urls.keys()):
            if col!='URL_ID' and col != 'URL':
                analyzed_urls[col].append(0)
    else:
        # Clean The article content
        article_content=remove_stopwords(article_content)
        
        # Tokenize the article contenct into sentences and words
        sentences, words = article_tokens(article_content)
        
        # Calculate the number of words(total and unique) and sentences
        word_count=len(words)
        sentence_count=len(sentences)
        unique_words=set(words)
        unique_word_count=len(unique_words)
        
        # Calculate the total number of characters
        char_count=0
        for word in words:
            char_count+=len(word)
        
        # Calculate derived values
        scores=calc_scores(words)
        
        # Calculate number of complex words and syllable count for each word
        complex_words, syllable_count = find_complex(words)
        complex_count=len(complex_words)
        total_syllable_count=0
        for word in syllable_count.keys():
            total_syllable_count+=syllable_count[word]
        
        # Calculate the number of personal pronouns
        pronoun_count=count_personal_pronouns(url_id)
        
        # Assign the values to the analysis variables
        analyzed_urls['URL_ID'].append(url_id)
        analyzed_urls['URL'].append(url)
        analyzed_urls['POSITIVE SCORE'].append(scores['POSITIVE SCORE'])
        analyzed_urls['NEGATIVE SCORE'].append(scores['NEGATIVE SCORE'])
        analyzed_urls['POLARITY SCORE'].append(scores['POLARITY SCORE'])
        analyzed_urls['SUBJECTIVITY SCORE'].append(scores['SUBJECTIVITY SCORE'])
        analyzed_urls['COMPLEX WORD COUNT'].append(complex_count)
        analyzed_urls['SYLLABLE PER WORD'].append(complex_count)
        analyzed_urls['WORD COUNT'].append(word_count)
        analyzed_urls['PERCENTAGE OF COMPLEX WORDS'].append(complex_count/unique_word_count)
        analyzed_urls['AVG SENTENCE LENGTH'].append(unique_word_count/sentence_count)
        analyzed_urls['FOG INDEX'].append(0.4 *(analyzed_urls['AVG SENTENCE LENGTH'][-1] + analyzed_urls['PERCENTAGE OF COMPLEX WORDS'][-1]))
        analyzed_urls['AVG NUMBER OF WORDS PER SENTENCE'].append(word_count/sentence_count)
        analyzed_urls['AVG WORD LENGTH'].append(char_count/word_count)
        analyzed_urls['PERSONAL PRONOUNS'].append(pronoun_count)
        
# Save the analyzes URLs
save_data(analyzed_urls,ofpath)
reformat(ofpath)
print("Data successfully saved in: "+ofpath)
