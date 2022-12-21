from PyPDF2 import PdfMerger


### Specify the order and names of the pdf in a list
pdfs = ["one.pdf", 'two.pdf', 'three.pdf']

merger  = PdfMerger()


########## In loop

for pdf in pdfs:
    merger.append(pdf)


########## Without loop
merger.append("one.pdf")
merger.append("two.pdf")
merger.append("three.pdf", pages=(0, 4, 2))

merger.write("merged.pdf")
merger.close()