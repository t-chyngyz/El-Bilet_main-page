from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from .forms import OfferForm, RequestForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView


# Create your views here.

# @login_required
class IndexView(TemplateView):
    template_name = "bilet/index.html"


class AboutUsView(TemplateView):
    template_name = "bilet/aboutus.html"


class ContactsView(TemplateView):
    template_name = "bilet/contacts.html"

class ServicesView(TemplateView):
    template_name = "bilet/services.html"

class RequestFormView(FormView):
    form_class = RequestForm
    template_name = 'bilet/requestforsurvey.html'
    success_url ="/"


class OffreFormView(FormView):
    form_class = OfferForm
    template_name = 'bilet/offer.html'
    success_url ="/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)

# def offer(request):
#     form = OfferForm()
#     return render(request,'bilet/offer.html', {'form':form})
