from annote_tokens import annote_txt

def calc_polarity_score(positive,negative):
    polarity_score=(positive-negative) / ((positive+negative) + 0.000001)
    return polarity_score

def calc_subjectivity_score(positive,negative,len_words):
    subjectivity_score = (positive+negative) / (len_words+0.000001)
    return subjectivity_score

def calc_scores(words):
    # Annotate each word with its sentiment score
    positive,negative=annote_txt(words)
    negative*=-1
    scores=dict()
    # Calculate POSITIVE, NEGATIVITY, POLARITY, SUBJECTIVITY SCORES
    scores['POSITIVE SCORE']=positive
    scores['NEGATIVE SCORE']=negative
    scores['POLARITY SCORE']=calc_polarity_score(positive,negative)
    scores['SUBJECTIVITY SCORE']=calc_subjectivity_score(positive,negative,len(words))
    return scores