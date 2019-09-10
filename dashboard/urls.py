from django.contrib import admin
from django.urls import path, include

from . import views, restAPIs

urlpatterns = [
    path('', views.dashHome, name='dashHome'),
    path('pendingReqsCount/', restAPIs.getPendingTransfersCount, name='pendingRequests'),
]
