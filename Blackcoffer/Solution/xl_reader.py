import openpyxl

def get_urls(file_path):

    # Load the Excel file
    workbook = openpyxl.load_workbook(file_path)

    # Choose a specific sheet by name
    sheet_name = 'Sheet1'
    sheet = workbook[sheet_name]

    # Create a dictionary to store the rows from the sheet
    url_dict =dict()
    b=0
    
    # Iterate through rows and columns to read data
    for row in sheet.iter_rows(values_only=True):
        if b==0:
            b+=1
        elif row[0]%1==0.0:
            url_dict[str(int(row[0]))] = row[1]
        else:
            url_dict[str(row[0])] = row[1]
        
    # Close the workbook when you're done
    workbook.close()

    return url_dict
