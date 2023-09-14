import re
from txt_reader import read_txt

def count_personal_pronouns(url_id):
    text=read_txt(url_id)
    text=text.replace('\n', '')
    
    # Define the pattern for personal pronouns
    pattern = r'\b(I|me|myself|my|you|yourself|your|he|him|himself|his|she|her|herself|hers|it|itself|we|us|ourselves|our|they|them|themselves|their|theirs)\b'

    # Use re.findall() to find all matches of personal pronouns
    personal_pronouns = re.findall(pattern, text, flags=re.IGNORECASE)
    
    # Count the personal pronouns
    personal_pronoun_count = len(personal_pronouns)

    return personal_pronoun_count
