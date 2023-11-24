
# opening encrypted file (decrypt)
import PyPDF2
pdfReader = PyPDF2.PdfReader(open('placeholder.pdf','rb'))
pdfReader.is_encrypted #'True' if file is encrypted 
pdfReader.decrypt('rosebud') #decrypt with known password 
pageObj = pdfReader.pages[0]
pageObj.extract_text()
