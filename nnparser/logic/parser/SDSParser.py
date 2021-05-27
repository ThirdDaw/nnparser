class SDSParser:
    def __init__(self, SDSfile):
        self.SDSfile = SDSfile

    def read_file(self):
        pass

    def check_file_format(self):
        return self.SDSfile.split("/")[-1].split(".")[-1]

    def get_filename(self):
        return self.SDSfile.split("/")[-1]

    def split_into_sections(self):
        pass
