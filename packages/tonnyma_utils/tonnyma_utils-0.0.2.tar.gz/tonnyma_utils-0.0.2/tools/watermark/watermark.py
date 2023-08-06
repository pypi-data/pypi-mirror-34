from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from StringIO import StringIO

# Use PyPDF to merge the image-PDF into the template
watermark = PdfFileReader(file('watermark.pdf', 'rb'))
doc = PdfFileReader(file("doc.pdf","rb"))

output = PdfFileWriter()
for i in range(doc.getNumPages()):
    page = doc.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

# set password
output.encrypt('datagroup', 'datagroup', True)

with open("output.pdf", "wb") as output_stream:
    output.write(output_stream)

print 'Done'
