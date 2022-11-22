from dataclasses import field
from pyexpat import model
from django import forms
from .models import Student


#class name always should start with Capital
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields =  '__all__'