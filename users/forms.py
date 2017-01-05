from django import forms
from Models import Course


class CreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['Name', 'Duration', 'Teacher', 'Value','Picture']
