#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pdfrw import PdfReader, PdfWriter
import glob

pdfs = glob.glob('*.pdf')

writer = PdfWriter()
for pdf in pdfs:
    writer.addpages(PdfReader(pdf).pages)
writer.write("PDF Join by Guerra.pdf")

