from django.contrib import admin
from django.urls import path, include

from . import views, restAPIs

urlpatterns = [
    path('', views.dashHome, name='dashHome'),
    path('budget/', views.budgetDisp, name='budgetPage'),
    path('budgetAddForm/', views.budgetAdd, name='budgetAddPage'),
    path('wbs/<int:budgetID>', views.wbsDisp, name='wbsPage'),
    path('wbs/<int:budgetID>/<int:namme>', views.wbsSpecificDisp, name='wbsSpecific'),
    path('pendingReqsCount/', restAPIs.getPendingTransfersCount, name='pendingRequests'),
]
