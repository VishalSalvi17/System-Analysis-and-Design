from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name="home"),
	path('contact.html',views.contact,name="contact"),
	path('destination.html',views.destination,name="destination"),
	path('about.html',views.about,name="about"),
]
