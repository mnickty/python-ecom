from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),     path('about', views.about, name="about"),
    path('tracker/', views.tracker, name="trackeringstatus"),
    path('search/', views.search, name="search"),
    path('checkout', views.checkout, name="checkout"),
    path('about', views.productview, name="productview"),
]
