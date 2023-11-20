
# creating document object 
import docx
doc = docx.Document('demo.docx')

# getting text from paragraph
import docx
doc = docx.Document('demo.docx')
len(doc.paragraphs)
doc.paragraph[0].text

# getting text from runs
import docx
doc = docx.Document('demo.docx')
len(doc.paragraphs[1].runs)
doc.paragraph[1].runs[3].text