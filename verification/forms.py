from django import forms
from django.forms import ModelForm
from .models import Verification
from django.contrib.auth.models import User

class UploadForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.HiddenInput()
        self.fields['username'].initial = User.objects.filter().first()
        
    username = forms.ModelChoiceField(
        queryset=User.objects.filter(),
        empty_label=None
    )
    category = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter item category'}))

    class Meta:
        model = Verification
        fields = ["username", "category", "form"]