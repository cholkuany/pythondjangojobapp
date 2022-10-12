from django import forms
from django.utils.translation import gettext_lazy as _

from subscribe.models import Subscribe

class Subscribe_Form(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields = '__all__'

        labels = {
            'first_name': _('Given Name'), 
            'last_name': _('Family Name'),
            'email': _('Email'),
        }
        error_messages = {
            'first_name': {
                'required': _('Give correct first name'),
                 }, 
        }


# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError(f'{value} contains a comma')
#     return value

# class Subscribe_Form(forms.Form):
#     first_name = forms.CharField(max_length=100, label='Given Name', validators=[validate_comma])
#     last_name  = forms.CharField(max_length=100, label='Family Name', validators=[validate_comma])
#     email      = forms.EmailField(max_length=100, validators=[validate_comma])