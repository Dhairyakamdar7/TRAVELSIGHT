from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  
from myapp import views
from myapp.views import get_reviews, submit_review


def redirect_to_index(request):
    return redirect('index')  # ✅ Redirect root URL to index/

urlpatterns = [
    path('', redirect_to_index, name='home'),  # ✅ Redirects / to /index/
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('an/', views.an, name='an'),
    path('ap/', views.ap, name='ap'),
    path('ap2/', views.ap2, name='ap2'),
    path('assam/', views.assam, name='assam'),
    path('bihar/', views.bihar, name='bihar'),
    path('chandigarh/', views.chandigarh, name='chandigarh'),
    path('chhattisgarh/', views.chhattisgarh, name='chhattisgarh'),
    path('delhi/', views.delhi, name='delhi'),
    path('diu/', views.diu, name='diu'),
    path('goa/', views.goa, name='goa'),
    path('gujarat/', views.gujarat, name='gujarat'),
    path('haryana/', views.haryana, name='haryana'),
    path('hp/', views.hp, name='hp'),
    path('jhk/', views.jhk, name='jhk'),
    path('jk/', views.jk, name='jk'),
    path('karnataka/', views.karnataka, name='karnataka'),
    path('kerala/', views.kerala, name='kerala'),
    path('ld/', views.ld, name='ld'),
    path('ll/', views.ll, name='ll'),
    path('maharashtra/', views.maharashtra, name='maharashtra'),
    path('manipur/', views.manipur, name='manipur'),
    path('meghalaya/', views.meghalaya, name='meghalaya'),
    path('mizoram/', views.mizoram, name='mizoram'),
    path('mp/', views.mp, name='mp'),
    path('nagaland/', views.nagaland, name='nagaland'),
    path('odisha/', views.odisha, name='odisha'),
    path('package/', views.package, name='package'),
    path('pdc/', views.pdc, name='pdc'),
    path('punjab/', views.punjab, name='punjab'),
    path('rajasthan/', views.rajasthan, name='rajasthan'),
    path('sikkim/', views.sikkim, name='sikkim'),
    path('telangana/', views.telangana, name='telangana'),
    path('tm/', views.tm, name='tm'),
    path('tripura/', views.tripura, name='tripura'),
    path('uk/', views.uk, name='uk'),
    path('up/', views.up, name='up'),
    path('wb/', views.wb, name='wb'),
    path('success/', views.success, name='success'),
    path('get_reviews/<int:blog_id>/', get_reviews, name='get_reviews'),
    path('submit_review/<int:blog_id>/', submit_review, name='submit_review'),
    path('myapp_stuff/', include('myapp.urls')),  # If you need myapp URLs
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]

