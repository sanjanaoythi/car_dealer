"""car_delar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
import home.views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('home/',home.views.home_view,name='home'),
    path('login/', home.views.login_view,name='login'),
    path('suvs/',home.views.suvs_view,name='suvs'),
    path('sedans/',home.views.sedans_view,name='sedans'),
    path('sports/',home.views.sports_view,name='sports'),
    path('convertibles/',home.views.convertibles_view,name='convertibles'),
    path('used/',home.views.used_view,name='used'),
    path('audi/',home.views.audi_view,name='audi'),
    path('toyota/',home.views.toyota_view,name='toyota'),
    path('bmw/',home.views.bmw_view,name='bmw'),
    path('landrover/',home.views.landrover_view,name='landrover'),
    path('mercedes/',home.views.mercedes_view,name='mercedes'),
    path('honda/',home.views.honda_view,name='honda'),
    path('payment/',home.views.payment_view,name='paymnet'),
    path('customer/',home.views.customer),
    path('order/',home.views.Order),
    path('payments/',home.views.Payment),
    path('',home.views.view,name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
