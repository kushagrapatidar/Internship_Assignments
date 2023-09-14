import requests
from bs4 import BeautifulSoup
from xl_reader import get_urls
from txt_saver import save_txt

#Change the file path as per the input file name
fpath="input.xlsx"

urls=get_urls(fpath)

no_title_lst=[]
no_text_lst=[]

for url_id in urls.keys():
    url=urls[url_id]

    # Fetch the webpage content
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the article title
    title_tag = soup.find('title')
    article_title = title_tag.get_text() if title_tag else ""

    # Find the article text
    article_text_tag = soup.find('div', class_='td-post-content')
    article_text=""
    if article_text_tag:
        # Remove the author from the article's contents
        for tag in article_text_tag.find_all('pre',{'class':'wp-block-preformatted'}):
            tag.extract()

        # Get the remaining content of the div
        article_text = article_text_tag.get_text(separator="\n")
        
    # Save the extracted title and text
    print("Saving: "+url_id)
    if article_text == "":
        no_text_lst.append(url_id)
    if article_title == "":
        no_title_lst.append(url_id)
        
    save_txt(url_id, article_title+'\n'+article_text)
    print("Saved: "+url_id)

#Print the URL_IDs of the files missing Article text or Article title
print("Missing Titles:", no_title_lst)
print("Missing Texts:", no_text_lst)
    
