import textract
import PyPDF2
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdf2image import convert_from_path

from nnparser.logic.ocr.OpticalCharacterRecognition import MultipleOpticalCharacterRecognition


class CVParser:
    def __init__(self, CVfile):
        self.CVfile = CVfile

    def read_file(self):
        if self.check_file_format() == 'doc' or self.check_file_format() == 'docx':
            data = textract.process(self.CVfile)

            print('RETURNING DOC OR DOCX DATA')
            return data
        elif self.check_file_format() == 'pdf':
            file = open(self.CVfile, 'rb')

            file_reader = PyPDF2.PdfFileReader(file)

            number_of_pages = file_reader.numPages

            data = ''
            for i in range(number_of_pages):
                data += file_reader.getPage(i).extractText()

            if data.strip() == '':
                output_string = StringIO()
                with open(self.CVfile, 'rb') as in_file:
                    pdf_parser = PDFParser(in_file)
                    doc = PDFDocument(pdf_parser)
                    resource_manager = PDFResourceManager()
                    device = TextConverter(resource_manager, output_string, laparams=LAParams())
                    interpreter = PDFPageInterpreter(resource_manager, device)
                    for page in PDFPage.create_pages(doc):
                        interpreter.process_page(page)

                data = output_string.getvalue()

                if self.data_is_valid(data):
                    print('RETURNING VALID PDF DATA')
                    return data
                else:
                    data = ''

                    images = convert_from_path(self.CVfile,
                                               poppler_path=r'C:\Users\ThreeDaws\Desktop\poppler-21.03.0\Library\bin')

                    filenames = []
                    for i in range(len(images)):
                        filename = ''.join(('tmp/', str(i + 10), '.jpg'))
                        images[i].save(filename)
                        filenames.append(filename)

                    ocr = MultipleOpticalCharacterRecognition(filenames)
                    for i in range(len(filenames)):
                        data += ocr.get_image_text(i)

                    print('RETURNING OCR PDF DATA')
                    return data
            else:
                print('RETURNING PDF DATA')
                return data

    def check_file_format(self):
        return self.CVfile.split("/")[-1].split(".")[-1]

    def get_filename(self):
        return self.CVfile.split("/")[-1]

    @staticmethod
    def split_into_sections(data):
        data = data.decode('utf-8')
        sections = data.split("\n\n\n\n")
        return sections

    # TODO validator
    @staticmethod
    def data_is_valid(data):
        return False
