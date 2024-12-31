from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings



urlpatterns = [    
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    
    
    path("password_change_done", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("reset-senha/", auth_views.PasswordResetView.as_view(template_name="registration/reset_senha_form.html"), name="reset_senha"),
]    
