from django.shortcuts import render

# Create your views here.

def dashHome(request):
    return render(request, 'dashboard/dashHome.html')
