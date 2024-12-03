# dwitter/urls.py

from django.urls import path
from django.conf.urls import include
from .views import dashboard, profile_list, profile
from django.contrib.auth import views as auth_views

app_name = "dwitter"
#https://stackoverflow.com/questions/76642163/django-urls-exceptions-noreversematch-reverse-for-password-reset-done-not-fou
urlpatterns = [
    path("", dashboard, name="dashboard"),
    #path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/', include(('django.contrib.auth.urls', 'auth'), namespace='accounts')),
    path('accounts/password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/password_reset_done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),name="password_reset"),
    #path('accounts/password_reset/password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),name="password_reset_done"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
]
