from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from myapp.forms import ContactForm   # Ensure the form is correctly imported




# ---------- Static Pages ----------
def about(request):
    return render(request, 'about.html')

def an(request):
    return render(request, 'an.html')

def ap(request):
    return render(request, 'ap.html')

def ap2(request):
    return render(request, 'ap2.html')

def assam(request):
    return render(request, 'assam.html')

def bihar(request):
    return render(request, 'bihar.html')

def chandigarh(request):
    return render(request, 'chandigarh.html')

def chhattisgarh(request):
    return render(request, 'chhattisgarh.html')

def contact(request):
    return render(request, 'contact.html')

def delhi(request):
    return render(request, 'delhi.html')

def diu(request):
    return render(request, 'diu.html')

def goa(request):
    return render(request, 'goa.html')

def gujarat(request):
    return render(request, 'gujarat.html')

def haryana(request):
    return render(request, 'haryana.html')

def hp(request):
    return render(request, 'hp.html')

def index(request):
    return render(request, 'index.html')

def jhk(request):
    return render(request, 'jhk.html')

def jk(request):
    return render(request, 'jk.html')

def karnataka(request):
    return render(request, 'karnataka.html')

def kerala(request):
    return render(request, 'kerala.html')

def ld(request):
    return render(request, 'ld.html')

def ll(request):
    return render(request, 'll.html')

def maharashtra(request):
    return render(request, 'maharashtra.html')

def manipur(request):
    return render(request, 'manipur.html')

def meghalaya(request):
    return render(request, 'meghalaya.html')

def mizoram(request):
    return render(request, 'mizoram.html')

def mp(request):
    return render(request, 'mp.html')

def nagaland(request):
    return render(request, 'nagaland.html')

def odisha(request):
    return render(request, 'odisha.html')

def package(request):
    return render(request, 'package.html')

def pdc(request):
    return render(request, 'pdc.html')

def punjab(request):
    return render(request, 'punjab.html')

def rajasthan(request):
    return render(request, 'rajasthan.html')

def sikkim(request):
    return render(request, 'sikkim.html')

def telangana(request):
    return render(request, 'telangana.html')

def tm(request):
    return render(request, 'tm.html')

def tripura(request):
    return render(request, 'tripura.html')

def uk(request):
    return render(request, 'uk.html')

def up(request):
    return render(request, 'up.html')

def wb(request):
    return render(request, 'wb.html')

def success(request):
    return render(request, 'success.html')  

