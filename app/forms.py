from django import forms

def check_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('Data is not valid')

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a])
    age=forms.IntegerField()
    email=forms.CharField(max_length=100)
    re_enter_email=forms.CharField(max_length=100)

