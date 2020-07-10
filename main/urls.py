
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('home/', views.homepage, name="homepage"),
    path('register/', views.register, name="register"),
    path('register/', views.register, name="register"),
    path('helpform/', views.helpform, name="helpform"),
    path('community/', views.community, name="community"),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name="login"),
]
