from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('personnel', views.personnel, name='personnel'),
    path('projects/complete', views.c_projects, name='c-projects'),
    path('projects/pending', views.p_projects, name='p-projects'),
    path('products', views.products, name='products')
]

