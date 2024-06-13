from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView ,DetailView ,CreateView,UpdateView ,DeleteView,FormView
from.models import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class Login(LoginView):
    template_name='login.html'
    fields='__all__'
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy('main:exam')
    
class Regiser(FormView):
    template_name='register.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('main:exam')
    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(Regiser,self).form_valid(form)
    
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main:exam')
        return super(Regiser,self).get(*args, **kwargs)
    