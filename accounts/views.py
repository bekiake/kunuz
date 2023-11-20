from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import UpdateView
from .models import User
from .forms import RegisterForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



class Register(View):
    
    def get(self, request):
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, "registration/regester.html", context)
    
    def post(self, request):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
        context = {
            'form': form
        }
        
        return redirect("accounts:login")
        
        
class MyProfileView(LoginRequiredMixin,View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        context = {
            'user': user
        }
        return render(request, "user/my_profile.html", context)
    

class MyProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "user/user_update.html"
    success_url = reverse_lazy("news:home")
    
    def test_func(self):
        new = self.get_object()
        if self.request.user == new.user or self.request.user.is_superuser:
            return True
        return False
    