from django import forms
from django.contrib.auth.models import User
from django.core import validators
from first_app.models import UserProfileInfo

class FeedbackForm(forms.Form): 
    title = forms.CharField(label = 'title', max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(label='subject',max_length=200, widget=forms.Textarea(attrs={'class':'form-control'}))
    email = forms.CharField(label = 'email', max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    #verify_email = forms.EmailField(label='Enter your email again:')
    botcatcher= forms.CharField(required=False,widget=forms.HiddenInput, validators= [validators.MaxLengthValidator(0)])    #we can use this or form.is_valid within views.py

    # def clean(self) :
    #     all_clean_data= super().clean()
    #     email = all_clean_data['email']
    #     verified_email = all_clean_data['verify_email']

    #     if email!=verified_email:
    #         raise forms.ValidationError('Make sure your emails match')


# class NewUserform(forms.ModelForm):
#     class Meta():
#         model=User
#         fields='__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput()) #edit attributes

    class Meta():
        model=User
        fields=('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():   #connects model to actual user profile info model
        model = UserProfileInfo
        fields=('portfolio_site','profile_pic')