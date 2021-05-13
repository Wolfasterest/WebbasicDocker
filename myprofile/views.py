import django
from django.contrib.auth.views import LoginView
from django.forms import fields, models, widgets
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UsernameField

class Login_view(LoginView):
    template_name ='./login.html'

'''class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields =('username','email')
        field_class = {'username':UsernameField}
        widgets ={
            'email':forms.EmailInput(attrs={'required':True})
        }'''

class Register_view(LoginView):
    template_name ='./register.html'
            
class myprofile_view(LoginRequiredMixin, TemplateView):
    template_name='./myprofile.html'