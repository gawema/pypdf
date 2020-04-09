from PyPDF2 import PdfFileWriter, PdfFileReader
import sys, os

pdf_reader = PdfFileReader(open(sys.argv[1], "rb"))
os.mkdir('./splitted_pages')

for pn in range (pdf_reader.getNumPages()):
	pdf_writer = PdfFileWriter()
	pdf_writer.addPage(pdf_reader.getPage(pn))
	split_file = open('./splitted_pages/split_file_'+str(pn)+'.pdf', 'wb')
	pdf_writer.write(split_file)
	split_file.close()
