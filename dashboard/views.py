from django.shortcuts import render

from .models import *
from .searializers import *

# Create your views here.

def dashHome(request):
    return render(request, 'dashboard/dashHome.html')
