from django.shortcuts import render

from app.models import app

# Create your views here.
def home_view(request):
    object_list = app.objects.all()
    return render(request, './index.html',{
        'object_list': object_list,
        'nav':'index'
    })
def websec_view(request):
    return render(request, './websec.html' ,{
        'nav':'Websec'
    })

def about_view(request):
    return render(request, './about.html' ,{
        'nav':'about'
    })
