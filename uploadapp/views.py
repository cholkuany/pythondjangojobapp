from django.shortcuts import render
from uploadapp.forms import UploadFileForm, UploadImageForm

from uploadapp.models import Upload_Image

# Create your views here.

def upload_image(request):
    form = UploadImageForm()
    context = {'form': form,}
    
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saved_object = form.instance
            context = {'form': form, 'saved_object': saved_object}
            return render(request, 'uploadapp/upload.html', context, )
  
    return render(request, 'uploadapp/upload.html', context)

def uploadFile(request):
    form = UploadFileForm()
    context = {'form': form,}
    
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saved_object = form.instance
            context = {'form': form, 'saved_object': saved_object}
            return render(request, 'uploadapp/file.html', context, )
  
    return render(request, 'uploadapp/file.html', context)