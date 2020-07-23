
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('home/', views.homepage, name="homepage"),
    path('register/', views.register_main, name="register_main"),
    path('register_student/', views.register_student, name="register_student"),
    path('register_tutor/', views.register_tutor, name="register_tutor"),
    path('helpform/', views.helpform, name="helpform"),
    path('community/', views.community, name="community"),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name="login"),
    path('profile/', views.profile, name='profile')
]
