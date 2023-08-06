"""gatehouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import gatehouseapp.views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('accounts/login/', auth_views.login, name='login'),
    path('accounts/logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    re_path(r'^$', gatehouseapp.views.homePage, name='home'),
    re_path(r'^gatehouseadmin/$', gatehouseapp.views.addVisit, name='appadmin'),
    re_path(r'^gatehousearch/$', gatehouseapp.views.archive, name='arch'),
    re_path(r'^delete/(?P<pk>\d+)$', login_required(gatehouseapp.views.VisitDelete.as_view()), name='delete'),
    re_path(r'^update/(?P<pk>\d+)$', login_required(gatehouseapp.views.UpdateVisitData.as_view()), name='update'),
    re_path(r'^todayvisit/$', login_required(gatehouseapp.views.TodayVisitForGatehouePersonListView.as_view()), name='todayvisit'),
    re_path(r'^updatearrive/(?P<pk>\d+)$', login_required(gatehouseapp.views.UpdateArriveHour.as_view()), name='update_arrive_hour'),
    re_path(r'^updateexit/(?P<pk>\d+)$', login_required(gatehouseapp.views.UpdateExitHour.as_view()), name='update_exit_hour'),
    re_path(r'^catering', login_required(gatehouseapp.views.CateringListView.as_view()), name='cateringurl'),
]
