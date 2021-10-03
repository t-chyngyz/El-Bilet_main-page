from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Электронная почта или имя пользователя', \
        widget=forms.TextInput(attrs={'class': \
        'entrance__inside-blocks__form__block-form__style-input-email'}))
    password = forms.CharField(label='Пароль', \
        widget=forms.PasswordInput(attrs={'class': \
        'entrance__inside-blocks__form__block-form__style-input-password'}))
