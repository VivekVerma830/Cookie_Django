from django.shortcuts import render


# Create your views here.

def set(request):
    data = render(request, 'set.html')
    data.set_cookie('name','Vivek')
    data.set_cookie('age','230')
    data.set_cookie('city','Bhopal')
    return data
