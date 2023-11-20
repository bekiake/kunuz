from django.urls import path
from .views import Register, MyProfileView, MyProfileUpdateView
from django.contrib.auth.views import LoginView, LogoutView


app_name = "accounts"
urlpatterns = [
    path("regester/", Register.as_view(), name="regester"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout" ),
    path('my_profile/', MyProfileView.as_view(), name='my_profile'),
    path('my_profile_update/<int:pk>', MyProfileUpdateView.as_view(), name='my_profile_update'),
]
