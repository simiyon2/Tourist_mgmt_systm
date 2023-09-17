"""
URL configuration for tourist_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include 
from tourist_app import views
from django.conf import settings 
from django.conf.urls.static import static 
from tourist_app.views import generate_pdf,generate_pdf_one,generate_pdf_two,generate_pdf_three,generate_pdf_four,generate_pdf_five,generate_pdf_six
from tourist_app.views import generate_pdf_seven
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.funindex, name='home'),
    path('login/', views.funlogin , name='login'), 
    path('logout/', views.funlogout , name='logout'),
    path('about/', views.funabout , name='about'),
    path('contact/', views.contact , name='contact'),
    path('destination/', views.fundestination , name='destination'),
    path('service/', views.funservice , name='service'),
    path('team/', views.funteam , name='team'),
    path('testimonial/', views.funtestimonial , name='testimonial'),
    path('package/', views.funpackage , name='package'),
    path('booking/', views.booking , name='booking'),

    path('funclog/', views.funclog, name='funclog'),
    # path('adminview/',views.regview),
    # path('regdelete/<id>',views.regdelete), 
    # path('regupdate/<id>',views.regupdate), 

    path('registration/', views.funcreg, name='registration'),

    path('thailand/',views.thailand,name='thailand'),
    path('indonesia/',views.indonesia,name='indonesia'),
    path('thailand/',views.thailand,name='thailand'),
    path('malaysia/',views.malaysia,name='malaysia'),

    path('london/',views.london,name='london'),
    path('singapore/',views.singapore,name='singapore'),
    path('japan/',views.japan,name='japan'),
    path('china/',views.china,name='china'),

    path('payment/',views.payment,name='payment'),
    path('payment_one/',views.payment_one,name='payment_one'),
    path('payment_two/',views.payment_two,name='payment_two'),
    path('payment_three/',views.payment_three,name='payment_three'),
    path('payment_four/',views.payment_four,name='payment_four'),
    path('payment_five/',views.payment_five,name='payment_five'),
    path('payment_six/',views.payment_six,name='payment_six'),
    path('payment_seven/',views.payment_seven,name='payment_seven'),
    
    path('privacy/',views.privacy,name='privacy'),
    path('generate_pdf/', generate_pdf, name='generate_pdf'),
    path('generate_pdf_one/', generate_pdf_one, name='generate_pdf_one'),
    path('generate_pdf_two/', generate_pdf_two, name='generate_pdf_two'),
    path('generate_pdf_three/', generate_pdf_three, name='generate_pdf_three'),
    path('generate_pdf_four/', generate_pdf_four, name='generate_pdf_four'),
    path('generate_pdf_five/', generate_pdf_five, name='generate_pdf_five'),
    path('generate_pdf_six/', generate_pdf_six, name='generate_pdf_six'),
    path('generate_pdf_seven/', generate_pdf_seven, name='generate_pdf_seven')
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
