import textract


class CVParser:
    def __init__(self, CVfile):
        self.CVfile = CVfile

    def read_file(self):
        pass

    def check_file_format(self):
        return self.CVfile.split("/")[-1].split(".")[-1]

    def get_filename(self):
        return self.CVfile.split("/")[-1]

    def split_into_sections(self):
        pass
