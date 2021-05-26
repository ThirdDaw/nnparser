import pytesseract
from PIL import Image


class OpticalCharacterRecognition:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def __init__(self, file):
        self.file = file

    def get_image_text(self):
        return pytesseract.image_to_string(Image.open(self.file))
