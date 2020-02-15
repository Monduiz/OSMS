"""OSMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import registration_view, logout_view, login_view
from main.views import HomeView
from users.views import (ProfileView, ProfileTripView, ProfileHoirView,
                            ProfileOscrView, ProfileCloseoutView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/trips/', ProfileTripView.as_view(), name='profile-trips'),
    path('profile/hoirs/', ProfileHoirView.as_view(), name='profile-hoirs'),
    path('profile/oscrs/', ProfileOscrView.as_view(), name='profile-oscrs'),
    path('profile/closeouts/', ProfileCloseoutView.as_view(), name='profile-closeouts'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('', include('main.urls')),

    # Password reset links taken from Django documentation (Github, auth views)
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'),
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_confirm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
]

# This will have to be modified for production.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
