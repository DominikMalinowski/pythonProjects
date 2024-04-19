"""Write a function named "decryptPdf()" that:
1. Takes path to PDF file as an argument
2. Decrypts given PDF file by brute force attack using words from "Chapter13dictionary.txt" file
   (You can find it in the Exercises catalog.
   Each line in this file = one word. Read these words into list object, then try to decrypt PDF using them)
3. Read only even pages (if there are 11 pages, only pages number 2,4,6,8,10 should be taken - be careful about that)
4. Creates new PDF file named "Output.pdf" in the Solutions catalog and puts there all read pages

Then, invoke this function with path to "Chapter13pdf.pdf" file (You can find it in the Exercises catalog)


Please:
- Use PyPDF2 module
- Try to use relative paths when doing some operations in different catalogs
- Don't commit created file
- Look at the last page of created PDF file to see something gorgeous"""

import PyPDF2

#  function definition
def decryptPdf():

    #  open following pdf file with pdf File reader
    pdfFile = PyPDF2.PdfFileReader(open('Chapter13pdf.pdf', 'rb'))

    #  check if pdf File is Encrypted
    if pdfFile.isEncrypted:

        print('\nThis document is encrypted.\nPlease wait, I am checking if your password is in below list:\n')
        #  read the whole file and split lines

        List = open("Chapter13dictionary.txt").read().splitlines()
        print(List)

        # decrypt for each element from the list
        for i in List:
            if pdfFile.decrypt(i) == 1:
                print('\nThe correct password was: "%s"' %i)
                #  break statement ends the loop containing it.
                #  If true, it goes to the instructions directly after the loop
                break
            else:
                #  continue statement is used to skip the rest of the code inside a loop for the current iteration only
                #  loop does not end, but continues with the next iteration
                continue
                #print('Password: "%s" is incorrect.' %i)
    else:
        print('This document is not encrypted')

    # check how many pages your pdf file has
    numPages = pdfFile.getNumPages()
    print('\nYour document has %i pages' % numPages)

    # creating new pdf file which represents a blank PDF document
    pdfWriter = PyPDF2.PdfFileWriter()

    # selecting only pages number 2,4,6,8,10
    for i in range(1, numPages, 2):

        # Get the Page object by calling getPage() and set it to pageObject
        pageObject = pdfFile.getPage(i)

        # Then pass that Page object to your PdfFileWriter’s addPage() method
        pdfWriter.addPage(pageObject)

    # write out the merged pdf
    with open('Output.pdf', 'wb') as out:
        pdfWriter.write(out)

    print('New document "%s" has been created' % out.name)

decryptPdf()