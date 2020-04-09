from PyPDF2 import PdfFileWriter, PdfFileReader
import sys, os
import fnmatch

dirpath = sys.argv[1]
npdf = len(fnmatch.filter(os.listdir(dirpath), '*.pdf'))
pdf_writer = PdfFileWriter()

for pn in range (npdf):
	pdf_reader = PdfFileReader(open(dirpath+'/split_file_'+str(pn)+'.pdf', "rb"))
	pdf_writer.addPage(pdf_reader.getPage(0))
merged_file = open('./merged_file.pdf', 'wb')
pdf_writer.write(merged_file)
merged_file.close()