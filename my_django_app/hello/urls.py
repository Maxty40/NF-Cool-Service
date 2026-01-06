from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('salam/', views.salam, name='salam'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('form_pemesanan/', views.form_pemesanan, name='form_pemesanan'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
]
