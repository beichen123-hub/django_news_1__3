from django.contrib import admin
from django.urls import path

from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', views.show, name='show'),
    path('add/', views.add, name='add'),
    path('insert/', views.insert, name='insert'),
    path('login/', views.login, name='login'),
    path('', views.register, name='register'),
    path('delete/<id>', views.delete, name='delete'),
]
