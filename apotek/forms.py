from django import forms
from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control mb-2'}),
#             'password': forms.PasswordInput(attrs={'class': 'form-control mb-2'})
#         }

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'username': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-2'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control mb-2'}),
        }
    
    conpassword = forms.CharField(
        label="Confirm Password",
        min_length=8, 
        max_length=255,
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-2'})
    )
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-2'}),
    )
    password = forms.CharField(
        min_length=8, 
        max_length=255,
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-2'})
    )

class SearchForm(forms.Form):
    search=forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search'}),
        required=False
    )



# class RegisterForm(forms.Form):
#     first_name = forms.CharField(max_length=255,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control mb-2'
#         })
#     )
#     last_name = forms.CharField(max_length=255, 
#         widget=forms.TextInput(attrs={
#             'class': 'form-control mb-2'
#         })
#     )

#     username = forms.CharField(
#         label="Username",
#         max_length=255, 
#         widget=forms.TextInput(attrs={
#             'class': 'form-control mb-2'
#         })
#     )

#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={
#             'class': 'form-control mb-2'
#         })
#     )
#     password = forms.CharField(
#         min_length=8, 
#         max_length=255,
#         widget=forms.PasswordInput(attrs={
#             'class': 'form-control mb-2'
#         })
#     )
#     conpassword = forms.CharField(
#         label="Confirm Password",
#         min_length=8, 
#         max_length=255,
#         widget=forms.PasswordInput(attrs={
#             'class': 'form-control mb-2'
#         })
#     )

#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'email', 'password']

