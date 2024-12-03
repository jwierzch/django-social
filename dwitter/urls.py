# dwitter/urls.py

from django.urls import path
from django.conf.urls import include
from .views import dashboard, profile_list, profile,index
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = "dwitter"
#https://stackoverflow.com/questions/66406530/keep-getting-this-error-of-reverse-for-password-reset-confirm-not-found-pass
urlpatterns = [
    path("dashboard", dashboard, name="dashboard"),
    path("", index, name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='dwitter/password_reset.html',success_url=reverse_lazy('dwitter:password_reset_done')),name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='dwitter/password_reset_done.html'), name='password_reset_done'),
]