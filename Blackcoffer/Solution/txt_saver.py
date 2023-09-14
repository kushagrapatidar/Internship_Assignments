
def save_txt(url_id, article_content):
        # Output filename
        file_path = 'Articles/'+url_id+'.txt'

        # Open the file in write mode ('w')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(article_content)
