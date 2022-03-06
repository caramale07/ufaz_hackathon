# Import required libraries

import PyPDF2
import textract
import re
import string
import pandas as pd
import matplotlib.pyplot as plt
  

def extract_text_from_pdf(filename):
    # Open pdf file
    pdfFileObj = open(filename,'rb')

    # Read file
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Get total number of pages
    num_pages = pdfReader.numPages

    # Initialize a count for the number of pages
    count = 0

    # Initialize a text empty etring variable
    text = ""

    # Extract text from every page on the file
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count +=1
        text += pageObj.extractText()

    return text 
