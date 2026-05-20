from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.register_page,name='register'),
    path('login/',views.login_page,name='login'),
    path('dashboard/',views.dashboard_page,name='dashboard'),
    path('logout/',views.logout_page,name='logout'),
    path('delete/<int:id>/', views.delete_task, name='delete'),
    path('update/<int:id>/', views.update_task, name='update')
]