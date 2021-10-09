from allauth.account.forms import LoginForm, SignupForm
from django import forms
import datetime
from country_utils.countries import COUNTRY_CHOICES
from .models import Profile

class MyCustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'].widget.attrs.update({
            'class': 'entrance__inside-blocks__form__block-form__style-input-email'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'entrance__inside-blocks__form__block-form__style-input-password'
        })

BIRTH_YEAR_CHOICES = ['1990', '1999', '2005']

class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='Имя', \
        widget=forms.TextInput(attrs={'class': \
        'registration__block__input-username', \
        'placeholder': 'Имя'})
        )
    last_name = forms.CharField(max_length=30, label='Фамилия', \
        widget=forms.TextInput(attrs={'class': \
        'registration__block__input-lastname', \
        'placeholder': 'Фамилия'})
        )
    birth_date = forms.DateField(label='Дата рождения', \
        widget=forms.NumberInput(attrs={'type': 'date', \
        'class':'registration__block__input-date'})
        )
    employment = forms.CharField(max_length=30, label='Вид занятости', \
        widget=forms.TextInput(attrs={'class': \
        'registration__block__input-employment', \
        'placeholder': 'Вид занятости'})
        )
    country = forms.CharField(max_length=30, label='Страна', \
        widget=forms.Select(choices=COUNTRY_CHOICES, attrs={'class': \
        'registration__block__input-country'})
        )
    region = forms.CharField(max_length=30, label='Область/Регион', \
        widget=forms.TextInput(attrs={'class': \
        'registration__block__input-rovince', \
        'placeholder': 'Область/Регион'})
        )

    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({
            'class': 'registration__block__input-email',
            'label': 'Электронная почта'
        })
        self.fields['email'].label = 'Электронная почта'

        self.fields['password1'].widget.attrs.update({
            'class': 'registration__block__input-password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'registration__block__input-password'
        })

        print (self.fields['email'].__dict__)

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        print(user.__dict__)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        profile = Profile(user = user, \
                        employment = self.cleaned_data['employment'], \
                        country = self.cleaned_data['country'], \
                        region = self.cleaned_data['region'], \
                        birth_date = self.cleaned_data['birth_date'], \
        )
        profile.save()
        user.save()
        return user
