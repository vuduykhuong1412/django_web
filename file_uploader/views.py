from distutils.command.upload import upload
from django.shortcuts import render
from django.db import models

from django.http import HttpResponse
from .forms import UploadFileForm

# Create your views here.
def fileUploaderView(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST , request.FILES)
        if form.is_valid():
            upload(request.FILES['file'])
            return HttpResponse("<h2 style=\"background-color:greenyellow\">File uploaded successful!</h2>")
        else:
            return HttpResponse("<h2 style=\"background-color:red\">File uploaded not successful!</h2>") 
            
    form = UploadFileForm()
    return render(request, 'fileUploaderTemplate.html',{'form':form})

# Sẽ thực hiện copy file vào thư mục gốc của server
def upload(f):
    file = open(f.name, 'wb+')
    for chunk in f.chunks():
        file.write(chunk)