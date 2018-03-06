from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contatos/<int:contact_id>/', views.detail, name='detail'),
    path('search/', views.search, name='contact_name')
]