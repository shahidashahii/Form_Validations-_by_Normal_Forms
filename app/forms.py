from django import forms
from django.core import validators

def check_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('Data is not valid')

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a])
    age=forms.IntegerField()
    email=forms.CharField(max_length=100)
    re_enter_email=forms.CharField(max_length=100)
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_email']
        if e!=r:
            raise forms.ValidationError('not matched')


    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot')
        
