from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import numpy as np

from .logic.parser.CVParser import CVParser
from .logic.ocr.OpticalCharacterRecognition import OpticalCharacterRecognition
from .logic.nn.CVNetwork import *


def index(request):
    return render(request, 'nnparser/index.html')


def cv(request):
    if request.method == "POST":
        data = request.POST
        files = request.FILES.getlist('file_field')

        for f in files:
            file_format = f.name.split(".")[-1]
            file_path = "".join(("tmp/2.", file_format))

            path = default_storage.save(file_path, ContentFile(f.read()))
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)

            parser = CVParser(tmp_file)

            saved_file_format = parser.check_file_format().lower()  # TODO delete lower
            saved_filename = parser.get_filename()

            if saved_file_format == "jpg" or saved_file_format == "jpeg" or saved_file_format == "png":
                ocr = OpticalCharacterRecognition(tmp_file)

                file_data = ocr.get_image_text()
            else:
                file_data = parser.read_file()

            sections = parser.split_into_sections(file_data)
            for section in sections[:4]:
                print(section)
                print("--------------------------------------------------")
            print(len(sections))

            # TODO fix :4 (cut 3 sections from doc)
            for section in sections[:4]:
                base_nn = BaseCVClassification()

                # TODO replace with generator
                nn_input = [0 for i in range(len(base_nn.keywords))]
                print(len(nn_input))
                for i in range(len(base_nn.keywords)):
                    if base_nn.keywords[i] in section.lower():
                        nn_input[i] = 1

                training_input = np.array([[0, 0, 0, 0],
                                           [0, 0, 0, 1]])
                training_output = np.array([[0, 1]]).T

                base_nn.train(training_input, training_output, 10000)

                print(nn_input)
                print(np.array(nn_input))
                print(base_nn.think(np.array(nn_input)))

                education_nn = EducationClassification()
                experience_nn = ExperienceClassification()
                skills_nn = SkillsClassification()
        # TODO nlp data
        metadata = ''

        # serialize

        # transfer into needed data format

    return render(request, 'nnparser/cv.html')


def sds(request):
    if request.method == "POST":
        data = request.POST
        files = request.FILES.getlist('file_field')

        for f in files:
            print(f)

    return render(request, 'nnparser/sds.html')
