from django import forms
from . models import Student
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class StudentForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Student
        fields = '__all__'