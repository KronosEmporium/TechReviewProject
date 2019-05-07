from django.urls import path
from . import views

urlpatterns = [
       path('', views.index, name='index'),
       path('gettypes/', views.gettypes, name = 'types'),
       path('getproducts/', views.getproducts, name = 'products'),
       path('getreviews/', views.getreviews, name = 'reviews'),
       path('productdetails/<int:id>', views.productdetails, name = 'productdetails'),
]