from django import forms

from .models import studentinfo
class studentdetails(forms.ModelForm):
    class Meta:
        model=studentinfo
        fields='__all__'