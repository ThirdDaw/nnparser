import textract
import PyPDF2
from tika import parser
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


class CVParser:
    def __init__(self, CVfile):
        self.CVfile = CVfile

    def read_file(self):
        if self.check_file_format() == 'doc' or self.check_file_format() == 'docx':
            data = textract.process(self.CVfile)

            return data
        elif self.check_file_format() == 'pdf':
            file = open(self.CVfile, 'rb')

            file_reader = PyPDF2.PdfFileReader(file)

            number_of_pages = file_reader.numPages

            data = ''
            for i in range(number_of_pages):
                data += file_reader.getPage(i).extractText()
                print(file_reader.getPage(i).extractText())

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

            return data

    def check_file_format(self):
        return self.CVfile.split("/")[-1].split(".")[-1]

    def get_filename(self):
        return self.CVfile.split("/")[-1]

    def split_into_sections(self):
        pass
