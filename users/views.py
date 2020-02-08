from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from users.forms import (RegistrationForm, UserAuthenticationForm,
                        UserUpdateForm, ProfileUpdateForm)
from main.models import Trip, Hoir, Oscr, Closeout
from django.views import View
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            messages.success(request, f'Account created for {username}')
            return redirect('login')
        else:
            context['registration_form'] = form
    else: # if its a get request
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('osms-landing')

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('osms-home')

    if request.POST:
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('osms-home')

    else:
        form = UserAuthenticationForm()
    context['form'] = form
    return render(request, 'users/login.html', context)

# CBV for profile
class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        trip_list = Trip.objects.filter(officer=request.user).order_by('-date_created')
        hoir_list = Hoir.objects.filter(officer=request.user).order_by('-date_created')
        oscr_list = Oscr.objects.filter(officer=request.user).order_by('-date_created')
        closeout_list = Closeout.objects.filter(officer=request.user).order_by('-date_created')

        # Pagination
        trips_paginator = Paginator(trip_list, 5)
        page_number = request.GET.get('page1', 1)
        trips_list = trips_paginator.page(page_number)

        hoir_paginator = Paginator(hoir_list, 5)
        page_number = request.GET.get('page2', 1)
        hoir_list = hoir_paginator.page(page_number)

        oscr_paginator = Paginator(oscr_list, 5)
        page_number = request.GET.get('page3', 1)
        oscr_list = oscr_paginator.page(page_number)

        closeout_paginator = Paginator(closeout_list, 5)
        page_number = request.GET.get('page4', 1)
        closeout_list = closeout_paginator.page(page_number)

        context = {
            'u_form': u_form,
            'p_form': p_form,
            'trip_list': trip_list,
            'trips_list': trips_list,
            'hoir_list': hoir_list,
            'oscr_list': oscr_list,
            'closeout_list': closeout_list
        }
        return render(request, 'users/profile.html', context)

    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account was updated.')
            return redirect('profile')


#FBV for profile
# @login_required
# def profile_view(request):
#
#     if request.POST:
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES, instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account was updated.')
#             return redirect('profile')
#
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#
#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#     return render(request, 'users/profile.html', context)
