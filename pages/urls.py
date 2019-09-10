from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    # path('register', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
