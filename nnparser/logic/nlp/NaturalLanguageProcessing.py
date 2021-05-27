import spacy


class CVProcessor:
    def __init__(self, data):
        self.data = data

    def generate_metadata(self):
        nlp = spacy.load('en_core_web_lg')

        handled_data = nlp(self.data.decode('utf-8'))
        metadata = {"person": '',
                    "knowledge and experience": ''}

        for entity in handled_data.ents:
            if entity.label_ == "PERSON":
                metadata["person"] = entity.text
            elif entity.label_ == "ORG" or entity.label_ == "PRODUCT":
                metadata["knowledge and experience"] = ' + '.join(
                    (metadata["knowledge and experience"], entity.text))

        return metadata
