from pdfrw import PdfReader, PdfWriter
import glob

pdfs = glob.glob('*.pdf')

writer = PdfWriter()
for pdf in pdfs:
    writer.addpages(PdfReader(pdf).pages)
writer.write("PDF Join by Guerra.pdf")

