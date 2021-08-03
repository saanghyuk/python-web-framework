from django import forms
from .models import Board


class BoardForm(forms.Form):
    title = forms.CharField(error_messages={
        "required": "Enter the title please"
    },
        max_length=128, label="Title")
    contents = forms.CharField(error_messages={
        "required": "Enter the contents please"
    }, widget=forms.Textarea, label="Contents")
    tags = forms.CharField(
        required=False, label="Tags Form"
    )
