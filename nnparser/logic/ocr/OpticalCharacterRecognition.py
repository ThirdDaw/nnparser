import pytesseract
from PIL import Image


class OpticalCharacterRecognition:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def __init__(self, file):
        self.file = file

    def get_image_text(self):
        return pytesseract.image_to_string(Image.open(self.file))


class MultipleOpticalCharacterRecognition:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def __init__(self, files):
        self.files = files

    def get_images_text(self):
        text = ''
        for image in self.files:
            image_text = pytesseract.image_to_string(Image.open(image))
            if image_text:
                text += image_text
        return text

    def get_image_text(self, image_number):
        return pytesseract.image_to_string(Image.open(self.files[image_number]))
