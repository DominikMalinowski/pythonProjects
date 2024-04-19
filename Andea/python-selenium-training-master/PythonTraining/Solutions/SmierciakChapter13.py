'''
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
'''

import PyPDF2

#Defining function for decryption
def decryptPdf(path):

#With loop for provided file. Must be opened in binary mode
    with open(path, "rb") as fi:

#Creating instance of PdfFileReader class for opened file
        pdf = PyPDF2.PdfFileReader(fi)

#Opening dictionary file
        with open("Chapter13dictionary.txt", "r") as passfi:
            print("Decrypting")

#Brute force loop
            for line in passfi:
                print(str(line.strip()))
                result = pdf.decrypt("nice") #str(line.strip()))

#Check if password is matching. If result = 1, then break the loop and store the password
#"1" stands for matching user password (permission for opening content), "2" stands for matching owner password (permissions for printing etc.)
                if result == 1:
                    password = str(line.strip())
                    break

#Get number of page
            noofpages = pdf.numPages

#Define new instance of PdfFileWriter
            newPDF = PyPDF2.PdfFileWriter()

#Loop for copying even pages
            for pdfpage in range(1,noofpages,2):
                newPDFpage = pdf.getPage(pdfpage)
                newPDF.addPage(newPDFpage)

#Write to file
            pdfOutputFile = open('Output.pdf',"wb")
            newPDF.write(pdfOutputFile)
            pdfOutputFile.close()


decryptPdf("Chapter13pdf.pdf")