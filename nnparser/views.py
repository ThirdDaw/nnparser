from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import FileFieldForm


class CVFileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = 'nnparser/cv.html'
    success_url = reverse_lazy('cv')

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        print(files)
        if form.is_valid():
            print("yes")
            for f in files:
                print(f)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def index(request):
    return render(request, 'nnparser/index.html')


def cv(request):
    if request.method == "POST":
        data = request.POST
        files = request.FILES.getlist('file_field')

        for f in files:
            print(f)

    return render(request, 'nnparser/cv.html')


def sds(request):
    if request.method == "POST":
        data = request.POST
        files = request.FILES.getlist('file_field')

        for f in files:
            print(f)

    return render(request, 'nnparser/sds.html')
