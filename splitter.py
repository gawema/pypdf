from PyPDF2 import PdfFileWriter, PdfFileReader


pdf_reader = PdfFileReader(open('/Users/gab/Desktop/mypdf.pdf', "rb"))
pdf_writer = PdfFileWriter()
pdf_writer.addPage(pdf_reader.getPage(0))
split_file = open('/Users/gab/Desktop/split_file.pdf', 'wb')
pdf_writer.write(split_file)
split_file.close()
