import json
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import numpy as np
import spacy

from .logic.parser.CVParser import CVParser
from .logic.parser.SDSParser import SDSParser
from .logic.ocr.OpticalCharacterRecognition import OpticalCharacterRecognition
from .logic.nn.CVNetwork import *
from .logic.utils.TrainingFileReader import TrainingFileReader
from nnparser.utils import *
from .logic.nlp.NaturalLanguageProcessing import CVProcessor


def index(request):
    return render(request, 'nnparser/index.html')


# TODO change files name to time
def cv(request):
    if request.method == "POST":
        data = request.POST
        files = request.FILES.getlist('file_field')

        for f in files:
            serialized = {"base": '',
                          "education": '',
                          "experience": '',
                          "skills": ''}

            file_format = f.name.split(".")[-1]
            file_path = "".join(("tmp/2.", file_format))

            path = default_storage.save(file_path, ContentFile(f.read()))
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)

            parser = CVParser(tmp_file)

            saved_file_format = parser.check_file_format().lower()
            saved_filename = parser.get_filename()

            if saved_file_format == "jpg" or saved_file_format == "jpeg" or saved_file_format == "png":
                ocr = OpticalCharacterRecognition(tmp_file)

                file_data = ocr.get_image_text()
            else:
                file_data = parser.read_file()

            sections = parser.split_into_sections(file_data)

            # TODO fix :4 (cut 3 sections from doc)

            for section in sections[:4]:
                base_result = base_nn_work(section)
                if base_result > 0.9:
                    if not serialized["base"]:
                        serialized["base"] = section
                        continue

                education_result = education_nn_work(section)
                if education_result > 0.9:
                    if not serialized["education"]:
                        serialized["education"] = section
                        continue

                experience_result = experience_nn_work(section)
                if experience_result > 0.9:
                    if not serialized["experience"]:
                        serialized["experience"] = section
                        continue

                skills_result = skills_nn_work(section)
                if skills_result > 0.9:
                    if not serialized["skills"]:
                        serialized["skills"] = section
                        continue

            nlp = CVProcessor(file_data)
            metadata = nlp.generate_metadata()

            resulting_file = {"data": serialized,
                              "metadata": metadata}

            with open('tmp/serialized/data.json', 'w') as json_file:
                json.dump(resulting_file, json_file)

    return render(request, 'nnparser/cv.html')


def sds(request):
    if request.method == "POST":
        data = request.POST
        files = request.FILES.getlist('file_field')

        for f in files:
            serialized = {"section1": None,
                          "section2": None,
                          "section3": None,
                          "section4": None,
                          "section5": None,
                          "section6": None,
                          "section7": None,
                          "section8": None,
                          "section0": None,
                          "section10": None,
                          "section11": None,
                          "section12": None,
                          "section13": None,
                          "section14": None,
                          "section15": None,
                          "section16": None, }

            file_format = f.name.split(".")[-1]
            file_path = "".join(("tmp/2.", file_format))

            path = default_storage.save(file_path, ContentFile(f.read()))
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)

            parser = SDSParser(tmp_file)

            saved_file_format = parser.check_file_format().lower()
            saved_filename = parser.get_filename()

    return render(request, 'nnparser/sds.html')
