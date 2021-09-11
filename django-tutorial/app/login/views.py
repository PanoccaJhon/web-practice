from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect

from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login
# Create your views here.


class LoginFormViewTemp(LoginView):
    template_name = 'login.html'
    
    def dispatch(self, request, *args, **kwargs):
        
        if request.user.is_authenticated:
            return redirect('store:category_list')
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Iniciar Sesión'
         
        return context

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('store:category_list')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('store:category_list')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Iniciar Sesión'
        return context
    