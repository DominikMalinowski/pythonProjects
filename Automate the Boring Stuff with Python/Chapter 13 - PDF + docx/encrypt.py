

import os 
import PyPDF2

cwd = os.getcwd()
extra_file_path = 'Andea\python-selenium-training-master\PythonTraining\Excercises\\bilet_ep_1897.pdf'
path_to_extra = os.path.join(cwd, extra_file_path)


def encrypt(file_to_crypt,password):
   pdfFile = open(file_to_crypt,'rb')
   pdfReader = PyPDF2.PdfReader(pdfFile)
   pdfWriter = PyPDF2.PdfWriter()

   for pageNum in range(len(pdfReader.pages)):
      pdfWriter.add_page(pdfReader.pages[pageNum])
   pdfWriter.encrypt(password)
   result_pdf = open(file_to_crypt,'wb')
   pdfWriter.write(result_pdf)
   result_pdf.close()

encrypt(extra_file_path,'and')