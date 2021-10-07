from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

# class LoginForm(forms.Form):
#     username = forms.CharField(label='Электронная почта или имя пользователя', \
#         widget=forms.TextInput(attrs={'class': \
#         'entrance__inside-blocks__form__block-form__style-input-email'}))
#     password = forms.CharField(label='Пароль', \
#         widget=forms.PasswordInput(attrs={'class': \
#         'entrance__inside-blocks__form__block-form__style-input-password'}))

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Электронная почта', \
        widget=forms.TextInput(attrs={'class': \
        'entrance__inside-blocks__form__block-form__style-input-email', \
        'placeholder': 'Email'}))
    password = forms.CharField(label='Пароль', \
        widget=forms.PasswordInput(attrs={'class': \
        'entrance__inside-blocks__form__block-form__style-input-password', \
        'placeholder':'Password'}))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', \
        widget=forms.PasswordInput(attrs={'class': \
        'entrance__inside-blocks__form__block-form__style-input-password', \
        'placeholder':'Password'}))
    password2 = forms.CharField(label='Пароль', \
        widget=forms.PasswordInput(attrs={'class': \
        'entrance__inside-blocks__form__block-form__style-input-password', \
        'placeholder':'Password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password2']
