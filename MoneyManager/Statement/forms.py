from django import forms
from .models import StatementUpload


class StatementUploadForm(forms.Form):
  csv = forms.FileField(label = 'Select a file', required=False)

