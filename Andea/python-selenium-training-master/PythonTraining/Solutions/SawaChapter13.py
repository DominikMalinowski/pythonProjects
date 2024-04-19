import PyPDF2

#riding password and crate list with password
def password():
    p = open('..\Excercises\Chapter13dictionary.txt', 'r')
    Pass = (p.read()).split('\n')
    p.close()
    return Pass
#decrypt pdf
def pdf():
    f = open('..\Excercises\Chapter13pdf.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(f)

    for i in password():
        if pdfReader.decrypt(i) != 1:
            pdfReader.decrypt(i)
        else:
            break
    return pdfReader

#create output (2,4,6,8,10 page)
def newPdf(pdfReader):
    output = PyPDF2.PdfFileWriter()
    noofpages = pdfReader.numPages
    for x in range(1, noofpages, 2):
        pageObj = pdfReader.getPage(x)
        output.addPage(pageObj)
    out = open('Output.pdf', 'wb')
    output.write(out)



pdfReader = pdf()
path=(r'..\Excercises\Chapter13pdf.pdf')
newPdf(pdfReader)