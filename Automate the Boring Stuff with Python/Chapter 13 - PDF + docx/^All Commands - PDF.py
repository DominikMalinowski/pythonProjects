
# loading PDF [
import PyPDF2
pdfFile = open('placeholder.pdf','rb')
pdfReader = PyPDF2.PdfReader(pdfFile)

# displaying text from page  
import PyPDF2
pdfReader = PyPDF2.PdfReader(open('placeholder.pdf','rb'))

pageObj = pdfReader.pages[0]
pageObj.extract_text()

# opening encrypted file (decrypt)
import PyPDF2
pdfReader = PyPDF2.PdfReader(open('placeholder.pdf','rb'))
pdfReader.is_encrypted #'True' if file is encrypted 
pdfReader.decrypt('rosebud') #decrypt with known password 
pageObj = pdfReader.pages[0]
pageObj.extract_text()

# combine two pdf file 
import PyPDF2
pdfReader1 = PyPDF2.PdfReader(open('to_combine.pdf','rb'))
pdfReader2 = PyPDF2.PdfReader(open('to_combine2.pdf','rb'))

pdfWriter = PyPDF2.PdfWriter()

    # adding pages from first file 
for pageNum in range(pdfReader.numPage):
    pageObj = pdfReader.pages[pageNum]
    pdfWriter.add_page(pageObj)
    
    # adding pages from second file 
for pageNum in range(pdfReader2.numPage):
    pageObj = pdfReader2.pages[pageNum]
    pdfWriter.add_page(pageObj)

pdfOutputFile = open('combinedFile','wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.closed

# page rotation 
import PyPDF2
pdfReader = PyPDF2.PdfReader(open('file_to_rotate.pdf','rb'))
page = pdfReader.pages[0]
page.rotateClockwise(90)
pdfWriter = PyPDF2.PdfWriter()
pdfWriter.add_page(page)
resultPdf = open('rotated_file.pdf','wb')
pdfWriter.write(resultPdf)
resultPdf.close()

# overlapping pages 
import PyPDF2
pdfReader = PyPDF2.PdfReader(open('placeholder.pdf','rb'))
pdfWatermark = PyPDF2.PdfReader(open('placeholder_watermark.pdf','rb'))
pdfReaderPage = pdfReader.pages[0]
pdfReaderPage.mergePage(pdfWatermark.pages[0])
pdfWriter = PyPDF2.PdfWriter()
pdfWriter.add_page(pdfReaderPage)
resultPdf = open('pdfMarked.pdf','wb')
pdfWriter.write(resultPdf)
resultPdf.close()

# encrypt PFD file 
import PyPDF2
pdfReader = PyPDF2.PdfReader(open('placeholder.pdf','rb'))
pdfWriter = PyPDF2.PdfWriter()
for pageNum in range(pdfReader.pages[pageNum]):
    pdfWriter.add_page(pdfReader.pages[pageNum])
pdfWriter.encrypt('password')
resultPdf = open('placeholder.pdf','wb')
pdfWriter.write(resultPdf)
resultPdf.close()