from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, "index.html", {})

def about_page(request):
    return render(request, "about.html", {})

def services_page(request):
    return render(request, "services.html", {})

def portfolio_page(request):
    return render(request, "portfolio.html", {})

def pricing_page(request):
    return render(request, "price.html", {})

def contact_page(request):
    return render(request, "contact.html", {})