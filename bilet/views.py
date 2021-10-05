from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

@login_required
def index(request):
    return render(request,'bilet/index.html')
#
