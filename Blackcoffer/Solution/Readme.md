Project Title and Description:
The objective of this assignment is to extract textual data articles from the given URL and perform text analysis to compute variables given below.
1. POSITIVE SCORE
2. NEGATIVE SCORE
3. POLARITY SCORE 
4. SUBJECTIVITY SCORE
5. AVG SENTENCE LENGTH
6. PERCENTAGE OF COMPLEX WORDS
7. FOG INDEX
8. AVG NUMBER OF WORDS PER SENTENCE
9. COMPLEX WORD COUNT
10. WORD COUNT
11. SYLLABLE PER WORD
12. PERSONAL PRONOUNS
13. AVG WORD LENGTH


Table of Contents:
1. Development_Log.txt file contains project timeline.
2. Text Extraction:
   	2.1. extractor.py:
		This file extracts the article content from the given urls and stores them in a .txt file in the Articles Folder.
		NOTE: Run this file only once before executing main.py

3. Text Analysis:
	3.1: main.py:
		This is the main execution file that countains the calls to below files and various analysis variables.
	3.2. clean_article.py:
		This file removes stopwords given in in StopWords folder and the punctuations from the article.
	3.3. tokenize_article.py:
		This file tokenizes the cleaned articles into sentences and  words.
	3.4. calc_derivedvar.py:
		This file calculates the derived variables for the article.
	3.5. complex_words:
		This file finds and calculates the number of syllables in a word and the number of complex words in the article.
	3.6. personal_pronouns.py:
		This file finds and calculates the number of personal pronouns in the article

4. Saving the analyzed data:
	4.1. xl_saver.py:
		This file saves the analyzed data to an excel spreadsheet and reformats the spreadsheet to the required formating.


Installation:
1. To run this project:
	1.1. Copy and paste the whole 'Solution' project folder into your system(except: articles' .txt files in the Articles Folder).
	1.2. Run the commands in install_dependencies file to install dependencies.
	1.3. Change the Input.xlsx file with your own url file in the same format.
	1.4. Run the extractor.py file only ones to extract your articles as .txt file.
	1.5. Now run the main.py file.
	1.6. Examine the analysis_output.py file for results.

2. Dependencies:
	2.1. Python Package Installer: PIP(PIP Installs Packages)
	2.2. General Python libraries
	2.3. 'BeautifulSoup' library
	2.4. 'requests' library
	2.5. 'openpyxl' library
	2.6. Regex library(i.e., re)
	2.7. String library
	2.8. NLTK:
		2.8.1. NLTK Library
		2.8.2. NLTK 'cmudict' corpus(English Pronunciation library)


Usage:
This project focuses on the analysis of article content of the article given on the website of url given in the Input.xlsx file.


Features:
1. Code Modulation
2. Re-usable codes
3. Easy to Modify
4. No complex calculations


License:
This project is solely purposed to evaluate the test assignment provided by Blackcoffer Micro Services Consulting for Data Science Internship. Hence, usage rather than author of the project and Blackcoffer Micro Services Consulting, is strictly prohibited. Leagal actions may be taken upon any illegal usage.

NOTE: For any Troubleshooting & QnAs, please contact the author.

Author Contact Information:
Kushagra Patidar
LinkedIn: https://www.linkedin.com/in/kushagra-patidar-3b2512125