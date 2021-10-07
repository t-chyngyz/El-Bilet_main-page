from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form.__dict__)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            print(user)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        print(form.__dict__)
    return render(request, 'account/login.html', {'form':form})

from django.contrib.auth import views as auth_views

class UserAuth(auth_views.LoginView):
    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        kwargs['form'] = LoginForm()
        return super().get_context_data(**kwargs)
    # authentication_form = LoginForm()

    # def get_form_class(self):
    #     return LoginForm()

def register(request):
    if request.method =='POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,
                        'registration/register_done.html',
                        {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'registration/register.html', {'user_form':user_form})
