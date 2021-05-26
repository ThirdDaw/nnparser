from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

from .logic.parser.CVParser import CVParser


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

            saved_file_format = parser.check_file_format()
            saved_filename = parser.get_filename()

            print(saved_file_format, saved_filename)

            # check if files are images or other format

            # if it is image - use ocr and nlp to translate into text file and then extract data
            # if pdf - extract data
            # if word - extract data

            # break into sections

            # create and learn networks
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
