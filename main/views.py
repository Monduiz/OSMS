from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import (DetailView, CreateView, UpdateView)
from django.views import View
from .models import Trip, Hoir, Oscr, Closeout, Office
from users.models import User
from main.utils import create_loc, create_trip_loc
from .forms import HoirForm, OscrForm, CloseoutForm
from geojson import Feature, FeatureCollection, dump
from django.contrib.gis.geos import Point
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

import json
import os
import pandas as pd

BASE_DIR = settings.BASE_DIR

# Used to load secrets
with open(os.path.join(BASE_DIR, 'OSMS/dev_secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)

def get_secret(setting, secrets=secrets):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))


def landing(request):
    return render(request, 'landing.html')

class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        trip_u = Trip.objects.filter(officer=request.user.id).last()
        hoir_u = Hoir.objects.filter(officer=request.user.id).last()
        oscr_u = Oscr.objects.filter(officer=request.user.id).last()
        closeout_u = Closeout.objects.filter(officer=request.user.id).last()

        context = {
        'trip_u': trip_u,
        'hoir_u': hoir_u,
        'oscr_u': oscr_u,
        'closeout_u': closeout_u
        }
        return render(request, 'main/home.html', context)

class TripDetailView(LoginRequiredMixin, DetailView):
    model = Trip

class TripCreateView(LoginRequiredMixin, CreateView):
    # Retrieves field names from model and removes ForeignKey and auto generated fields
    trip_fields = [f.name for f in Trip._meta.fields]
    trip_fields = [e for e in trip_fields if e not in ('id', 'officer', 'date_created')]

    model = Trip
    fields = trip_fields



    def get_context_data(self, **kwargs):
        algolia_ID = get_secret('ALGOLIA_PLACES_ID')
        algolia_token = get_secret('ALGOLIA_PLACES_KEY')
        algolia_ID_json = json.dumps(algolia_ID)
        algolia_token_json = json.dumps(algolia_token)
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['algolia_ID_json'] = algolia_ID_json
        context['algolia_token_json'] = algolia_token_json
        return context

    def get_initial(self):
        initial = super(TripCreateView, self).get_initial()
        user = self.request.user
        initial['firstname'] = self.request.user.firstname
        initial['lastname'] = self.request.user.lastname
        return initial

    def form_valid(self, form):
        form.instance.officer = self.request.user
        return super().form_valid(form)

class TripUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # Retrieves field names from model and removes ForeignKey and auto generated fields
    trip_fields = [f.get_attname() for f in Trip._meta.fields]
    trip_fields = [e for e in trip_fields if e not in ('id', 'officer', 'date_created')]

    model = Trip
    fields = trip_fields

    def form_valid(self, form):
        form.instance.officer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        trip = self.get_object()
        if self.request.user == trip.officer:
            return True
        return False


class HoirDetailView(LoginRequiredMixin, DetailView):
    model = Hoir

class HoirCreateView(LoginRequiredMixin, CreateView):
    form_class = HoirForm
    model = Hoir

    def get_initial(self):
        initial = super(HoirCreateView, self).get_initial()
        user = self.request.user
        initial['firstname'] = self.request.user.firstname
        initial['lastname'] = self.request.user.lastname
        return initial

    def form_valid(self, form):
        form.instance.officer = self.request.user
        return super().form_valid(form)

class HoirUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # Retrieves field names from model and removes ForeignKey and auto generated fields
    # hoir_fields = [f.get_attname() for f in Hoir._meta.fields]
    # hoir_fields = [e for e in hoir_fields if e not in ('id', 'officer', 'date_created')]
    form_class = HoirForm
    model = Hoir


    def form_valid(self, form):
        form.instance.officer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        hoir = self.get_object()
        if self.request.user == hoir.officer:
            return True
        return False

class OscrCreateView(LoginRequiredMixin, CreateView):
    form_class = OscrForm
    model = Oscr

    def get_initial(self):
        initial = super(OscrCreateView, self).get_initial()
        user = self.request.user
        initial['firstname'] = self.request.user.firstname
        initial['lastname'] = self.request.user.lastname
        return initial

    def form_valid(self, form):
        form.instance.officer = self.request.user
        return super().form_valid(form)

class OscrDetailView(LoginRequiredMixin, DetailView):
    model = Oscr

class CloseoutCreateView(LoginRequiredMixin, CreateView):
    form_class = CloseoutForm
    model = Closeout

    def form_valid(self, form):
        form.instance.officer = self.request.user
        return super().form_valid(form)

class CloseoutDetailView(LoginRequiredMixin, DetailView):
    model = Closeout

class OfficeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        #offices = Office.objects.all().order_by('city')

        # API secrets
        map_token = get_secret('MAPBOX_TOKEN')
        mapbox_token = json.dumps(map_token)


        off_locations = create_loc()

        feature_collection = FeatureCollection(off_locations)

        context = {
            'offices': feature_collection,
            'mapbox_token': mapbox_token
        }
        return render(request, 'main/offices.html', context)

class DashView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        trip_u = Trip.objects.filter(officer=request.user.id).all()
        trip_loc = Trip.objects.filter(officer=request.user.id).values('dest_name', 'dest_address', 'dest_city', 'dest_province', 'dest_postal_code', 'dest_lng', 'dest_lat')
        df_all = pd.DataFrame(list(Trip.objects.filter(officer=request.user.id).values()))
        # df = pd.DataFrame.from_records(Trip.objects.filter(officer=request.user.id).values_list('risk_score_label'))
        df2 = df_all['risk_score_label'].value_counts()
        df3 = df_all['legislation'].value_counts()
        df4 = df_all['risk_weapons'].value_counts()
        df2 = df2.to_json(orient='columns')
        df3 = df3.to_json(orient='columns')
        df4 = df4.to_json(orient='columns')

        trip_locations = create_trip_loc(trip_u)
        trip_feature = FeatureCollection(trip_locations)

        context = {
        'df2': df2,
        'df3': df3,
        'df4': df4,
        'trip_loc': trip_feature,
        }
        return render(request, 'main/dash.html', context)
