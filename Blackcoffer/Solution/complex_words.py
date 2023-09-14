from nltk.corpus import cmudict
# Initialize the CMU Pronouncing Dictionary
pronouncing_dict = cmudict.dict()

# Function to count syllables in a word
def count_syllables(word):
    if len(word) > 3 and word[-2] == 'e' and (word[-1] == 's' or word[-1] == 'd'):
        word = word[:-2]
    if word.lower() in pronouncing_dict:
        # The dictionary entry is a list of possible pronunciations
        # Each pronunciation is a list of phonemes, where each phoneme is separated by a space
        # Counting the number of phonemes gives the number of syllables
        return max([len([ph for ph in pron if ph[-1].isdigit()]) for pron in pronouncing_dict[word.lower()]])
    else:
        # If the word is not found in the dictionary, a simple fallback is to count vowels
        # This may not be accurate for all words
        return max([word.lower().count(vowel) for vowel in 'aeiou'])

# Function to find complex words


def find_complex(words):
    syllable_count = dict()
    complex_words = []
    for word in words:
        if word not in syllable_count:
            syllable_count[word] = count_syllables(word)
            if syllable_count[word] > 2 and word not in complex_words:
                complex_words.append(word)
    return complex_words, syllable_count
