
# loading PDF 
import PyPDF2
pdfFile = open('placeholder.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

# displaying text from page  
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('placeholder.pdf','rb'))

pageObj = pdfReader.getPage(0)
pageObj.extractText()

# openig encrypted file   
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('placeholder.pdf','rb'))
pdfReader.isEncrypted #'True' if file is encrypted 
pdfReader.decrypt('rosebud') #decrypt with known password 
pageObj = pdfReader.getPage(0)
pageObj.extractText()

# combine two pdf file 
import PyPDF2
pdfReader1 = PyPDF2.PdfFileReader(open('to_combine.pdf','rb'))
pdfReader2 = PyPDF2.PdfFileReader(open('to_combine2.pdf','rb'))

pdfWriter = PyPDF2.PdfFileWriter()

    # adding pages from first file 
for pageNum in range(pdfReader.numPage):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    
    # adding pages from second file 
for pageNum in range(pdfReader2.numPage):
    pageObj = pdfReader2.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedFile','wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.closed

# page rotation 
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('file_to_rotate.pdf','rb'))
page = pdfReader.getPage(0)
page.rotateClockwise(90)
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdf = open('rotated_file.pdf','wb')
pdfWriter.write(resultPdf)
resultPdf.close()

# overlapping pages 
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('placeholder.pdf','rb'))
pdfWatermark = PyPDF2.PdfFileReader(open('placeholder_watermark.pdf','rb'))
pdfReaderPage = pdfReader.getPage(0)
pdfReaderPage.mergePage(pdfWatermark.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(pdfReaderPage)
resultPdf = open('pdfMarked.pdf','wb')
pdfWriter.write(resultPdf)
resultPdf.close()

# encrypt PFD file 
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('placeholder.pdf','rb'))
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.getPage(pageNum)):
    pdfWriter.addPage(pdfReader.getPage(pageNum))
pdfWriter.encrypt('password')
resultPdf = open('placeholder.pdf','wb')
pdfWriter.write(resultPdf)
resultPdf.close()