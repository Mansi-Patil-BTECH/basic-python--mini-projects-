from pypdf import PdfWriter
merger = PdfWriter()
# import pypdf
# merger = pypdf.PdfWriter()

pdfs = ["unit1.pdf", "unit2.pdf"]
for pdf in pdfs:
    merger.append(pdf)

merger.write("merge.pdf")

#more to code