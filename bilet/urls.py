from django.urls import path
from .views import OffreFormView, IndexView, AboutUsView, ContactsView, \
                    RequestFormView, ServicesView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    path('aboutus/', AboutUsView.as_view(), name='aboutus'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('services/', ServicesView.as_view(), name='services'),
    path('requestforsurvey/', RequestFormView.as_view(), name='requestforsurvey'),
    path('offer/', OffreFormView.as_view(), name='offer'),
]
