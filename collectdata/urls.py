
from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    
    path('',views.home,name='home'),
    path('login/', views.login_request, name="login"),
    path("details/", views.Details, name="details"),
    path('add_form/',views.add_form,name='add_form'),
    path("logout/", views.logout_request, name="logout"),
    path("distance/", views.get_distance, name="distance"),
    path("boostangel_post", views.post_boostangel, name="boostangel"),


    
]
