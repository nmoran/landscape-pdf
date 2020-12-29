import PyPDF2 as pdf
import sys
import copy

def convert_to_landscape(fn, out_fn, verbose=False):
    reader = pdf.PdfFileReader(fn)
    reader2 = pdf.PdfFileReader(fn)
    writer = pdf.PdfFileWriter()

    number_pages = reader.getNumPages()
    for pn in range(number_pages):
        if verbose: print(f'Onto page {pn}')
        page = reader.getPage(pn)
        # page2 = copy.deepcopy(page)
        page2 = reader2.getPage(pn)
        b = page.cropBox
        ar = b[3]/b[2]
        crop_height = int(b[2]/ar)
        # print(f"{ar}, {crop_height}")
        page.rotateCounterClockwise(90)
        page.cropBox = pdf.generic.RectangleObject([0, b[3]-crop_height, 612, b[3]])
        writer.addPage(page)
        page2.rotateCounterClockwise(90)
        page2.cropBox = pdf.generic.RectangleObject([0, 0, 612, crop_height])
        writer.addPage(page2)

    if verbose: print("Done processing pages and now writing them to the file")
    with open(out_fn, "wb") as io:
        writer.write(io)

    if verbose: print("All done")

