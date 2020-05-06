"""Urban_Street_Cleanliness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static

from Urban_Street_Cleanliness import settings
from users import views as user_views
from managements import views as managements_views

urlpatterns = [
    url('admin/', admin.site.urls),


url(r'^$',user_views.userslogin, name='userslogin'),
url(r'^registers',user_views.registers, name='registers'),
url(r'^myaccounts',user_views.myaccounts, name='myaccounts'),
url(r'^feedback',user_views.feedback, name='feedback'),
url(r'^garbagereport',user_views.garbagereport, name='garbagereport'),
url('viewresult',user_views.viewresult,name="viewresult"),
url('yourreport',user_views.yourreport,name="yourreport"),
url(r'^userslogout',user_views.userslogout, name='userslogout'),


url(r'^managementlogin$',managements_views.managementlogin, name='managementlogin'),
url(r'^usersdetails$',managements_views.usersdetails, name='usersdetails'),
url(r'^viewfeedback$',managements_views.viewfeedback, name='viewfeedback'),
url(r'^uploadfiles$',managements_views.uploadfiles, name='uploadfiles'),
url(r'^viewreport$',managements_views.viewreport, name='viewreport'),
url(r'^viewmap/(?P<pk>\d+)/$',managements_views.viewmap,name="viewmap"),
url(r'^statusprocess/(?P<pk>\d+)$',managements_views.statusprocess, name="statusprocess"),
url(r'^userscheck$',managements_views.userscheck, name='userscheck'),
url(r'^graphanalysis/(?P<chart_type>\w+)', managements_views.graphanalysis, name="graphanalysis"),
url(r'^managementlogout$',managements_views.managementlogout, name='managementlogout'),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
