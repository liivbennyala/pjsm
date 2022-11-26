from django.urls import path
from . import views

urlpatterns = [
   path('',views.store, name ='store'),
   path('checkout/', views.checkout, name='checkout'),
   path('about/', views.about, name = 'about'),
   path('contact/', views.contact, name='contact'),
   path('index/', views.index, name='index'),
   path('product/', views.index, name='product'),
   path('service/', views.index, name='service'),
   path('single/', views.index, name='single'),
]



  