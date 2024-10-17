from django import forms
from research.models import researchpapers

class paperform(forms.ModelForm):
    class Meta :
            model=researchpapers
            fields="__all__"

