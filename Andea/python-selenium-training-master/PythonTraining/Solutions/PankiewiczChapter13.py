# V 1.0 - 22.05.2019
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

# import PyPDF2 to work with PDF files
import PyPDF2 as Pdf

# PDF file- relative path (.. means “the parent folder.”)
# (r') or (\\ in path) means that it is link to a file, not a ordinary string
path = (r'..\Excercises\Chapter13pdf.pdf')

# dictionary file- relative path
dictionary = ('..\\Excercises\\Chapter13dictionary.txt')

# connecting every word in dictionary to call in 'list' variable
with open(dictionary, 'r') as f:
    passwords = [line.strip() for line in f]

# opening variable for PDF file in 'read binary' mode
pdf_open = open(path, 'rb')

# PDF reading variable
pdf_read = Pdf.PdfFileReader(pdf_open)


def printing_writing_file():
    # create variable with number of pages of original PDF file
    number_of_pages = pdf_read.numPages
    # PDf writing variable
    pdf_write = Pdf.PdfFileWriter()

    # for 'n' between 1 and (last_page_of_PDF),increment by 2 (so 2,4,6,...) do:
    for n in range(1, number_of_pages, 2):
        # variable currently taken page of original PDF
        page_obj = pdf_read.getPage(n)
        # printing of page from PDF file with 'page_object' number
        print(page_obj.extractText())
        # adds page with current 'page_obj' number at the end of 'pdf_write' variable
        pdf_write.addPage(page_obj)

    # create new variable with name 'PDF Digits.pdf' in (write binary) mode
    pdf_new_file = open('PDF Digits.pdf', 'wb')
    # create new PDF file for 'pdf_new_file' variable
    pdf_write.write(pdf_new_file)


def decrypting_file():
    # if PDF file is not encrypted
    if not pdf_read.isEncrypted:
        print("File not encrypted!")

    # if PDF file is encrypted and password is needed
    else:
        print("File is encrypted. Decoding- please wait")
        # for i <= number_of_passwords, do:
        for i in range(len(passwords)):
            # has file been decrypted by using this particular password? ("1"-YES, "0"-NO)
            success = pdf_read.decrypt(passwords[i])

            # if decrypted- print password and go out from "if-else" block
            if success == 1:
                print('Succes! Password: ' + str(passwords[i]) + '\n')
                break
            # if not decrypted- end "if-else" block and take another value of "i" (i += 1)
            else:
                continue


# call both functions
decrypting_file()
printing_writing_file()
# close currently opened PDF file
pdf_open.close()
