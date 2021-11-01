# import fitz
# doc = fitz.open('test.pdf')
# print(doc.metadata)
# page = doc.load_page(0)
# print(page.get_text())
# res=page.search_for("Full Name", hit_max=0)
# print(len(res))
# create raster image of page (non-transparent)
# pm = page.get_pixmap(matrix=trans, alpha=False)
# for r in res:
#     print

''' 1 . convert pdf to img '''

import  fitz  # import the bindings

# doc = fitz.open('test.pdf')  # open document
# for page in doc:  # iterate through the pages
#     pix = page.get_pixmap()  # render page to an image
#     pix.save("page-%i.png" % page.number)  # store image as a PNG

''' 2. convert doc to pdf'''
# doc = fitz.open('test.pdf')  # open document
# pdfbytes = doc.convert_to_pdf()
# pdf = fitz.open("pdf", pdfbytes)
# pdf.save('updated.pdf')

''' 3. Insert Image into pdf'''

# doc = fitz.open('test.pdf')  # open document

# page = doc[0]
# d = page.get_text("dict")
# blocks = d["blocks"]
# imgblocks = [b for b in blocks if b["type"] == 1]
# print(imgblocks[0].rect)

# rect = page.search_for('FULL NAME')
# page.show_pdf_page(rect[0], 'sample.pdf')
# doc.save("update.pdf")

''' We have used pymupdf module for the pdf munpulation, you can install it using
    this link https://pymupdf.readthedocs.io/en/latest/installation.html
'''
import fitz


REPLACEMENT_DICT = {
    '{FULL NAME}': 'JOHN TURNE',
    '{number1}': '123456',
    '{number2}': 'AA123456',
    '{date11111}': '17/12/2021'
}

# DEFINE COLORS
white = (1,1,1)
blue = (0, 0, .6)

def process_pdf(doc):
    output_folder = 'result.pdf'
    replace_image_folder = 'download.jpg'
    # now read the page
    page = doc.loadPage(0)

    #TEXT REPLACEMENT
    for rep_key, rep_value in REPLACEMENT_DICT.items():
        text_instances = page.searchFor(rep_key)
        for inst in text_instances:
                    text_point = fitz.Point(inst[0], inst[3])
                    # Creating a white strip
                    shape = page.newShape()  # create Shape
                    shape.draw_rect(inst)
                    shape.finish(color = white, fill = white)
                    # Intsert the replacement TEXT over the strip
                    shape.insertText(text_point, rep_value, color = blue)
                    shape.commit()

    # Insert Image:
    # Get the rect dynamically here
    img_rect = fitz.Rect(275.385009765625, 696.5970458984375, 339.5159912109375, 760.72802734375)
    shape = page.newShape()  # create Shape
    shape.draw_rect(img_rect)
    shape.finish(color = white, fill = white)
    shape.commit()
    page.insertImage(img_rect, filename=replace_image_folder )

    # save final doc here
    doc.save(output_folder, garbage=4, deflate=True, clean=True)

if __name__ == "__main__":
    # Get the pdf file
    input_folder = 'test.pdf' #define your input path here
    doc = fitz.open(input_folder)  # open document
    process_pdf(doc)
