from allauth.account.forms import LoginForm

class MyCustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'].widget.attrs.update({
            'class': 'entrance__inside-blocks__form__block-form__style-input-email'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'entrance__inside-blocks__form__block-form__style-input-password'
        })
