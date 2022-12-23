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


#import
import PyPDF2


#path (file name) to pdf and password
path = 'Chapter13pdf.pdf'
pathDic = 'Chapter13dictionary.txt'


#create list with password
file = open(pathDic)
passwd = (file.read()).split('\n')


#decrypt pdf
def decrypt (path):
    pdfReader = PyPDF2.PdfFileReader(open(path, 'rb'))
    for i in passwd:
        if pdfReader.decrypt(i) != 1:
            pdfReader.decrypt(i)
        else:
            break
    return pdfReader



#put pages 2,4,6,8,10 to "output.pdf"
def newPdf ():
    #create output
    outputfile = open('output.pdf', 'wb')
    output = PyPDF2.PdfFileWriter()
    for j in (2,4,6,8,10):
        pageObj = pdfReader.getPage(j-1)
        print(pageObj.extractText())
        pageObj.extractText()
        output.addPage((pageObj))

    output.write(outputfile)
    outputfile.close()


pdfReader = decrypt(path)
newPdf()
