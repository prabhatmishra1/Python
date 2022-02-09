import qrcode
import cv2
import pathlib
import os

# Get current file path
current_path = pathlib.Path(__file__).parent.absolute()
output_folder = os.path.join(current_path, 'output')

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


def generate_qr(obj=None, output_filename=None):
    # it return image
   img = qrcode.make(obj)
   output_file_path = os.path.join(current_path, 'output', output_filename)
   img.save(output_file_path)

''' we can read QR code using opencv module '''

import cv2
def decode_qr(img):
    d = cv2.QRCodeDetector()
    value, point, qr =  d.detectAndDecode(cv2.imread(img))
    print(value)
if __name__ == "__main__":
   generate_qr(obj='8300016', output_filename='Scottijohn_Test.png')
   print("done")
#    print("decoding.......")
#    decode_qr('D:\python\socket_programming\QRCODE\output\mrn.png')
