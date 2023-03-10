from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import service
from .models import Document, Department
from .forms import DocumentForm


def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'documents/index.html', context)


def documents(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            service.save_file(form)
        return HttpResponseRedirect('/documents')
    else:
        context = {
            'title': 'Документы',
            'documents': Document.objects.all(),
            'form': DocumentForm()
        }
        return render(request, 'documents/document.html', context)
