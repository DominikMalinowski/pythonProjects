"""
Write a function named "decryptPdf()" that:
1. Takes path to PDF file as an argument
2. Decrypts given PDF file by brute force attack using words from "Chapter13dictionary.txt" file (You can find it in the Exercises catalog.
   Each line in this file = one word. Read these words into list object, then try to decrypt PDF using them)
3. Read only even pages (if there are 11 pages, only pages number 2,4,6,8,10 should be taken - be careful about that)
4. Creates new PDF file named "Output.pdf" in the Solutions catalog and puts there all read pages

Then, invoke this function with path to "Chapter13pdf.pdf" file (You can find it in the Exercises catalog)


Please:
- Use PyPDF2 module
- Try to use relative paths when doing some operations in different catalogs
- Don't commit created file
- Look at the last page of created PDF file to see something gorgeous
"""

import os 
import PyPDF2

pdf_file_path = 'Andea\python-selenium-training-master\PythonTraining\Excercises\Chapter13pdf.pdf'
pass_file_path = 'Andea\python-selenium-training-master\PythonTraining\Excercises\Chapter13dictionary.txt'
new_file_pass = 'Andea\Exercise_13'

cwd = os.getcwd()
path_to_PDF = os.path.join(cwd, pdf_file_path)
path_to_pass = os.path.join(cwd, pass_file_path)
path_to_new = os.path.join(cwd, new_file_pass)

# Function to brute force decryption of PDF file via words from .txt file 
# parameter: documentToDecrypt - path to PDF file that gonna be brute force decrypted 
# parameter: file_with_pass - path to .txt file with words for brute force decryption

def decryptPdf(documentToDecrypt, file_with_pass):
   pdfReader = PyPDF2.PdfReader(open(documentToDecrypt,'rb'))

   # open file with possible passwords 
   opened_file_with_pass = open(file_with_pass,'r') 

   # saving saving content into list 
   decrypt_list = opened_file_with_pass.read().splitlines()

   #good
   for word in decrypt_list:
  
      # if statement to notify when file got encrypted 
      if pdfReader.decrypt(word) != False:
         print("Password is: " + word)
         break
      else:
         continue
   return word

print(decryptPdf(path_to_PDF, path_to_pass))

# Function to create new file by using even pages of old one 
# parameter: path to 
# parameter: file_with_pass - path to .txt file with words for brute force decryption

def new_pdf(old_file,destination_path):
   pdfReader = PyPDF2.PdfReader(open(old_file,'rb'))
   pdfWriter = PyPDF2.PdfWriter()
   pdfReader.decrypt('nice')

   for pageNum in range(len(pdfReader.pages)):
      if (pageNum%2 == 1):
         pageObj = pdfReader.pages[pageNum]
         pdfWriter.add_page(pageObj)
      else:
         continue
   
   location = (os.path.join(destination_path,'Output.pdf'))
   outPutPDF = open(location,'wb')
   pdfWriter.write(outPutPDF)
   outPutPDF.close()


new_pdf(path_to_PDF,path_to_new)