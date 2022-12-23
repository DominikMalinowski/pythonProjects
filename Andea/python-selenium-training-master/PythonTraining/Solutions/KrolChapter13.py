import PyPDF2, os
from pathlib import Path


def decryptPdf(PDFpath):
    pdf_file = open(PDFpath, 'rb')  # Open PDF file
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    if not pdf_reader.isEncrypted:
        return print('This pdf file is not encrypted')

    p = Path(PDFpath)  # Path to file
    os.chdir(p.parent)  # set current working directory to same as pdf file

    # Open dictionary and create a list of the decryption content
    dictionary = open('Chapter13dictionary.txt', 'r')
    decrypt_list = dictionary.read().splitlines()

    for word in decrypt_list:
        if pdf_reader.decrypt(word) != 1:
            # print(word + ' doesn\'t work')
            continue
        else:
            pdf_reader.decrypt(word)
            print(p.name + ' has been decrypted with word: ' + word)
            break
    return pdf_reader


def createPDFeven(pdf_to_change):
    pdf_file = open(pdf_to_change, 'rb')  # Open PDF file
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)  # Read that PDF file
    if pdf_reader.isEncrypted:  # decrypt file if needed
        pdf_reader = decryptPdf(pdf_to_change)

    pdf_writer = PyPDF2.PdfFileWriter()  # Virtual creation of PDF file
    for pageNum in range(1, pdf_reader.numPages + 1):
        if pageNum % 2 == 0:
            pdf_writer.addPage(pdf_reader.getPage(pageNum - 1))

    Output_File = open(r'..\Solutions\Output.pdf', 'wb')
    pdf_writer.write(Output_File)
    print('Output.pdf file has been created')


# Calling decrypt pdf function for Chapter13pdf.pdf file

# decryptPdf(r'..\Excercises\Chapter13pdf.pdf')
createPDFeven(r'..\Excercises\Chapter13pdf.pdf')
