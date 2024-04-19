import PyPDF2

def password():
    f=open('..\Excercises\Chapter13dictionary.txt', 'r')

    #reading from file
    text=f.read()
    #spliting string to list
    content=text.split('\n')
    f.close()
    return content


def decryptPdf(path):

    content=password()
    #opening pdf file
    pdfReader = PyPDF2.PdfFileReader(open(path, 'rb'))

    #brute force
    i=0
    while pdfReader.decrypt(content[i])!=1:
        print(content[i])
        i+=1


    #creating output file
    pdfOutputFile = open('output.pdf', 'wb')
    pdfOutput=PyPDF2.PdfFileWriter()

    #reading and copy data from pdf file
    for i in (2,4,6,8,10):
        pageObj = pdfReader.getPage(i-1)
        print(pageObj.extractText())
        pdfOutput.addPage(pageObj)
    #save and close output file
    pdfOutput.write(pdfOutputFile)
    pdfOutputFile.close()


path=(r'..\Excercises\Chapter13pdf.pdf')
decryptPdf(path)