from django import forms
from django.contrib.auth.forms import UserCreationForm  
from .models import User   
# class RegisterForm(forms.Form):
#     username = forms.CharField(max_length=255)
#     email = forms.EmailField()
#     first_name = forms.CharField(max_length=255)
#     last_name = forms.CharField(max_length=255)
#     phone = forms.CharField(max_length=255)
#     adress = forms.CharField(max_length=255)
#     password = forms.CharField(widget=forms.PasswordInput())
#     password_confirm = forms.CharField(widget=forms.PasswordInput())

    # def save():
    #     pass
    
    

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'address','avatar', 'password1', 'password2']
        
        
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'address','avatar']