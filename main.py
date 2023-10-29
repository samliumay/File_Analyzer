import os
import re
import PyPDF2
import docx
import openpyxl

# Global variables for file location and content
file_location = ""
file_content = ""    

# Function to read the content of the file based on its extension
def read_file(file_location):
    # Get the file extension from the file location
    _, file_extension = os.path.splitext(file_location)
    file_content = ""

    if file_extension == ".pdf":
        # If the file is a PDF
        pdf_file = open(file_location, "rb")
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        file_content = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            file_content += page.extractText()
        pdf_file.close()
    elif file_extension == ".docx":
        # If the file is a DOCX (Word) document
        doc = docx.Document(file_location)
        file_content = ""
        for paragraph in doc.paragraphs:
            file_content += paragraph.text
    elif file_extension == ".xlsx":
        # If the file is an Excel spreadsheet
        wb = openpyxl.load_workbook(file_location)
        file_content = ""
        for sheet in wb.worksheets:
            for row in sheet.iter_rows(values_only=True):
                for cell_value in row:
                    file_content += str(cell_value) + "\n"
    elif file_extension == ".txt":
        # If the file is a plain text file
        file_location = file_location.replace("\\","/")
        file = open(file_location,"r")
        file_content = file.read()
    else:
        # For other file types, you can add handling methods or display an error message.
        print("This file type is not supported")

    return file_content

# Function to look for email addresses in the file content
def lookForMails_in_file(file_content):    
    match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', file_content)
    x = 1
    for i in match:
        print("Mail-"+ str(x) +": "  +i)
        x = x + 1

# Other functions can be added as needed.

# Main program
print("Hello, Please enter the file location:")
file_location = input("File location:")
file_content = read_file(file_location)
lookForMails_in_file(file_content)
