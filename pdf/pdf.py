import PyPDF2
import sys

# include as many pdfs as we can
inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()  # merger object
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')


pdf_combiner(inputs)

template = PyPDF2.PdfFileReader(open('pdf/super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('pdf/watermark.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

# getNumPages returns the number of pages available
for i in range(template.getNumPages()):
    page = template.getPage(i)  # get the current page
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('pdf/watermarked_output.pdf', 'wb') as file:
        output.write(file)


# we are reading the binary of the file object
# with open('pdf/test.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     # write in binary
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('crooked.pdf', 'wb') as new_file:
#         writer.write(new_file)
