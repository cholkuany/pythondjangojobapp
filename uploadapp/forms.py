
from django import forms
from django.utils.translation import gettext_lazy as _

from uploadapp.models import Upload_Image, UploadFiles

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Upload_Image
        fields = '__all__'

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFiles
        fields = '__all__'
