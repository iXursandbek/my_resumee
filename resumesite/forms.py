from django import forms
from .models import *
from ckeditor.fields import RichTextField


class ResumeForm(forms.ModelForm):
    #userName = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    #title = forms.CharField(widget=forms.TextInput(),required=True, max_length=100)
    description = RichTextField()

    class Meta:
        model  = Resume
        fields = ('description',)