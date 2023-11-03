from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginn,name='login'),
    path('signup', views.signupp,name='signup'),
    path('logout', views.logoutt,name='logout'),
    path('adminlogin', views.adminloginn,name='adminlogin'),
    path('crud', views.crudd,name='crud'),
    path('usr',views.user_logout,name='usr'),
    path('add', views.addd, name='add'),
    # path('edit', views.editt, name='edit'),
    path('update/<str:id>', views.Update, name='update'),
    path('delete/<str:id>', views.deletee, name='delete'),
    path('search', views.searchh, name='search'),
    
]
