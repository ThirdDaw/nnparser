class TrainingFileReader:
    def __init__(self, path):
        self.path = path

    def read_file(self):
        with open(self.path) as file:
            data = file.readlines()
            return data

    @staticmethod
    def get_training_input(data):
        input_data = []
        for line in data:
            input_data.append(list(line.split("-")[0]))

        return input_data

    @staticmethod
    def get_training_output(data):
        output_data = []
        for line in data:
            output_data.append(int(line.split("-")[-1]))

        return output_data
