import fitz
import pathlib
import os
from progress.bar import Bar
import pdb

# Get current file path
current_path = pathlib.Path(__file__).parent.absolute()

# Create input and output folders if doesn't exist
input_folder = os.path.join(current_path, 'input')
output_folder = os.path.join(current_path, 'output')
if not os.path.exists(input_folder):
    os.makedirs(input_folder)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


REPLACEMENT_DICT = {
    'ABC': 'AWS',
    'NBG': 'AWS',
    'Nucor Buildings Group': 'AMERICAN WESTERN STEEL',
    'AMERICAN BUILDINGS COMPANY': 'AMERICAN WESTERN STEEL',
    '10%': '25%'
}

FONT_FILE_DICT = {
    'SegoeUI,Bold':'SegoeUIBold.ttf',
    'SegoeUI,BoldItalic':'SegoeUIBoldItalic.ttf',
    'SegoeUI,Italic':'SegoeUIItalic.ttf',
    'SegoeUI,Regular':'SegoeUI.ttf',
}

# page_logo_filename = '/Users/kaushikdr/workspace/freelance/hamza/assets/AWS-LOGO-Perect-Large-Tran-1200-NEW.png'
# watermark_new = '/Users/kaushikdr/workspace/freelance/hamza/assets/AWS_watermark.png'
# watermark_filename = '/Users/kaushikdr/workspace/freelance/hamza/assets/watermark_new.pdf'
# watermark = fitz.open(watermark_filename)

# DEFINE COLORS
white = (1,1,1)
black = (0,0,0)

#DEFINE FILENAME AND Open Last Page PDF.
page_logo_filename = '/Users/kaushikdr/workspace/freelance/hamza/assets/AWS_header_logo.png'
last_page_logo_filename = '/Users/kaushikdr/workspace/freelance/hamza/assets/LOGO.pdf'
last_logo_pdf = fitz.open(last_page_logo_filename)


def process_pdf(filename):
    """
    This method will be used to process all changes to the PDF.
    """
    input_file = os.path.join(current_path, 'input', filename)
    current_pdf = fitz.open(input_file)

    with Bar('Processing', max=len(current_pdf)) as bar:
        # Compute the Font information from the page and it's individual blocks.
        for current_page in range(len(current_pdf)):
            page = current_pdf.loadPage(current_page)
            page_font_bbox_dict = {}
            blocks = page.get_text("dict", flags=11)["blocks"]
            for block in blocks:  # iterate through the text blocks
                for line in block["lines"]:  # iterate through the text lines
                    for span in line["spans"]:
                        page_font_bbox_dict.update({(span['bbox'][1],
                            span['bbox'][3]): {'text':span['text'],
                            'font':span['font'], 'fontsize':span['size'],
                            'fontcolor':span['color']}})

            #TEXT REPLACEMENT
            for rep_key, rep_value in REPLACEMENT_DICT.items():
                text_instances = page.searchFor(rep_key)
                for inst in text_instances:
                    rect_text = page.getTextbox(inst)
                    #GET FONT INFO HERE using the Y-coordinates
                    font_info = page_font_bbox_dict.get((inst[1],inst[3]))

                    # Default Textpoint
                    text_point = fitz.Point(inst[0], inst[3])
                    #FONTFILE
                    fontfile = '/Users/kaushikdr/workspace/freelance/hamza/assets/fonts/'+ FONT_FILE_DICT.get(font_info['font'])
                    fontsize = font_info['fontsize']

                    #CUSTOMISATION ACC to KEY
                    if rep_value == 'AWS':
                        text_point = fitz.Point(inst[0]-1, inst[3]-2)
                    elif rep_value == 'AMERICAN WESTERN STEEL':
                        if fontsize < 9:
                            if 'Bold' in font_info['font']:
                                text_point = fitz.Point(inst[0]-1, inst[3]-2)
                                fontsize = font_info['fontsize'] - 1.5
                            else:
                                text_point = fitz.Point(inst[0], inst[3]-1.5)
                        else:
                            if 'Bold' in font_info['font']:
                                text_point = fitz.Point(inst[0], inst[3]-2.4)
                                fontsize = font_info['fontsize'] - .5
                            else:
                                text_point = fitz.Point(inst[0]-1, inst[3]-2.2)
                    else:
                        text_point = fitz.Point(inst[0], inst[3]-2)

                    # Creating a white strip
                    shape = page.newShape()  # create Shape
                    shape.draw_rect(inst)
                    shape.finish(color = white, fill = white)
                    # Intsert the replacement TEXT over the strip
                    shape.insertText(text_point, rep_value, color = black,
                        fontsize=fontsize, fontname=font_info['font'], fontfile=fontfile)
                    shape.commit()

            #HEADER CHANGE
            # watermark_rect = fitz.Rect(60,20,page.rect.tr.x-100,page.rect.br.y-100)

            if not current_page == len(current_pdf)-1:
                #TOP LEFT
                page_logo_rect = fitz.Rect(30, 25, 320, 96)
                shape.draw_rect(page_logo_rect)
                #TOP RIGHT
                shape.draw_rect(fitz.Rect(498, 40, 585, 70))
                shape.finish(color = white, fill = white)
                shape.commit()
                page.insertImage(page_logo_rect, filename=page_logo_filename)

                buyers_acceptance_page = page.search_for("BUYER'S ACCEPTANCE")
                if buyers_acceptance_page:
                    buyers_acceptance_rect = buyers_acceptance_page[0]
                    shape.draw_rect(fitz.Rect(30, buyers_acceptance_rect[1]-5, 320, buyers_acceptance_rect[3]+20))
                    seller_rect = page.search_for("For SELLER")[0]
                    seller_logo_rect = fitz.Rect(30, seller_rect[1]-8, seller_rect[0]-10, seller_rect[3]+28)
                    shape.draw_rect(seller_logo_rect)
                    shape.finish(color = white, fill = white)
                    shape.commit()
                    page.insertImage(seller_logo_rect, filename=page_logo_filename)
                # page.show_pdf_page(watermark_rect, watermark, overlay=False)
                # page.insertImage(watermark_rect, filename=watermark_new, overlay=False)

            else:
                images = page.get_images()
                if images:

                    current_rot = page.rotation
                    page.setRotation(current_rot - 90)
                    # last_page_logo_rect = fitz.Rect(1130, 90, 1211, 240)
                    last_page_logo_rect = fitz.Rect((page.rect.tr.x-94), 90, page.rect.tr.x - 13, 240)
                    page.show_pdf_page(last_page_logo_rect, last_logo_pdf, rotate=90, keep_proportion=False)
                    # page.show_pdf_page(page.rect, watermark, overlay=False, rotate=90)
                    current_rot = page.rotation
                    page.setRotation(current_rot + 90)
            bar.next()

    output_filename = 'output_'+filename
    output_file_path = os.path.join(current_path, 'output', output_filename)
    current_pdf.save(output_file_path, garbage=4, deflate=True, clean=True)

    # CLOSE THE CURRENTLY OPENED PDF FILES TO REMOVE IT FROM MEMORY
    current_pdf.close()
    last_logo_pdf.close()
    print("Processing Complete! Please check the output directory for the corrected PDF File.")

    # watermark.close()


if __name__ == "__main__":
    # Get the pdf file
    input_filename = input('\nInput the PDF file name: ')
    process_pdf(input_filename)

