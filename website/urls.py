from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("",views.home,name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('Products/',views.Products,name='Products'),
    path('AnnualReports/',views.AnnualReports,name='AnnualReports'),
    path('Announcements/',views.Announcements,name='Announcements'),
    path('Boardofdirectors/',views.Boardofdirectors,name='Boardofdirectors'),
    path('Branch/',views.Branche,name='Branche'),

] 
