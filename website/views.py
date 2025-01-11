from django.http import HttpResponse
from django.shortcuts import render
from .models import director
from .models import Product
from .models import NewsandUpdate
from .models import Branch
from .models import AnnualReport
from .models import HomeSlide
from .models import Aboutus
from .models import Byelaw
from .models import Announcement
import media


def home(request):
    Byelaws=Byelaw.objects.all()
    Homeslide=HomeSlide.objects.all()
    Products=Product.objects.all()
    directors=director.objects.all()
    Newsandupdates = NewsandUpdate.objects.all()
    n=len(Newsandupdates)
    params = {'Newsandupdates': Newsandupdates,range:range(n),'Product': Products,'director':directors,'Homeslide':Homeslide,'Byelaw':Byelaws}
    return render(request,'website/home.html',params)

def aboutus(request):
    Byelaws=Byelaw.objects.all()
    Homeslide=HomeSlide.objects.all()
    About=Aboutus.objects.all()
    n=len(Homeslide)
    params = {'Product': Products,'range':range(n),'Homeslide':Homeslide,'About':About,'Byelaw':Byelaws}
    return render(request,'website/aboutus.html',params)

def Products(request):
    Byelaws=Byelaw.objects.all()
    Products=Product.objects.all()
    Homeslide=HomeSlide.objects.all()
    n=len(Products)
    params = {'Product': Products,'range':range(n),'Homeslide':Homeslide,'Byelaw':Byelaws}
    return render(request,'website/products.html',params)

def AnnualReports(request):
    Byelaws=Byelaw.objects.all()
    Homeslide=HomeSlide.objects.all()
    AnnualReports=AnnualReport.objects.all()
    n=len(AnnualReports)
    params={'AnnualReport':AnnualReports,range:range(n),'Homeslide':Homeslide,'Byelaw':Byelaws}
    return render(request,'website/annualreport.html',params)

def Announcements(request):
    Announcements=Announcement.objects.all()
    Byelaws=Byelaw.objects.all()
    Homeslide=HomeSlide.objects.all()
    Products=Product.objects.all()
    directors=director.objects.all()
    Newsandupdates = NewsandUpdate.objects.all()
    n=len(Newsandupdates)
    params = {'Newsandupdates': Newsandupdates,range:range(n),'Product': Products,'director':directors,'Homeslide':Homeslide,'Byelaw':Byelaws,'Announcement':Announcements}
    return render(request,'website/announcements.html',params)


def Branche(request):
    Byelaws=Byelaw.objects.all()
    Homeslide=HomeSlide.objects.all()
    Branchs=Branch.objects.all()
    n=len(Branchs)
    params={'Branch':Branchs,range:range(n),'Homeslide':Homeslide,'Byelaw':Byelaws}
    return render(request,'website/branches.html',params)

def Boardofdirectors(request):
    Byelaws=Byelaw.objects.all()
    Homeslide=HomeSlide.objects.all()
    directors=director.objects.all()
    n=len(directors)
    params = {'director': directors,'range':range(n),'Homeslide':Homeslide,'Byelaw':Byelaws}
    return render(request,'website/boardofdirectors.html',params)