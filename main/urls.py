from django.urls import path
from .views import (TripDetailView, TripCreateView, TripUpdateView,
                    HoirDetailView, HoirCreateView, OscrCreateView,
                    OscrDetailView, CloseoutCreateView, CloseoutDetailView,
                    OfficeView, HoirUpdateView, HomeView, DashView)
from . import views

urlpatterns = [
    path('', views.landing, name='osms-landing'), # landing goes here
    path('home/', HomeView.as_view(), name='osms-home'),
    path('dash/', DashView.as_view(), name='dash'),
    path('trip/<int:pk>/', TripDetailView.as_view(), name='trip-detail'),
    path('trip/new/', TripCreateView.as_view(), name='trip-create'),
    path('trip/<int:pk>/update/', TripUpdateView.as_view(), name='trip-update'),
    path('trip/<int:pk>/print/', TripUpdateView.as_view(template_name='main/trip_print.html'), name='trip-print'),
    path('hoir/<int:pk>/', HoirDetailView.as_view(), name='hoir-detail'),
    path('hoir/new/', HoirCreateView.as_view(), name='hoir-create'),
    #path('hoir/<int:pk>/update/', HoirUpdateView.as_view(), name='hoir-update'),
    path('hoir/<int:pk>/print', HoirUpdateView.as_view(template_name='main/hoir_print.html'), name='hoir-print'),
    path('oscr/new/', OscrCreateView.as_view(), name='oscr-create'),
    path('oscr/<int:pk>/', OscrDetailView.as_view(), name='oscr-detail'),
    path('closeout/new', CloseoutCreateView.as_view(), name='closeout-create'),
    path('closeout/<int:pk>/', CloseoutDetailView.as_view(), name='closeout-detail'),
    path('offices/', OfficeView.as_view(), name='osms-offices'),
]
