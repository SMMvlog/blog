from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('search/', views.search, name="search"),
    path('signup', views.signup, name="signup"),
    path('login', views.Login, name="login"),
    path('logout', views.Logout, name="logout"),
    path('about/', views.about, name="about"),
]