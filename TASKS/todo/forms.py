from .models import Task
from django import forms

class modelform(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'prio', 'date']

    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))