from django.shortcuts import render
from django.core.mail import send_mail
from .models import Location, Hotel
from accounts import views
from django.views.generic import View


class Locations(View):
	template_name = 'home.html'	
	
	def displayLocation(self, request, *args, **kwargs):
		locs = Location.objects.all()

		return render(request,self.template_name,{'locs': locs})

def home(request):

	locs = Location.objects.all()

	return render(request,'home.html',{'locs': locs})

class ContactUs(View):

	def post(self, request):

		name_var = request.POST.get('name')
		email_var = request.POST.get('email')
		subject_var = request.POST.get('subject')
		message_var = request.POST.get('message')
		
		send_mail(
			subject_var,
			message_var,
			email_var,
			['shivampawar515@gmail.com'],
		)

		return render(request,'contact.html',{'name_var':name_var})




def contact(request):
	if request.method == "POST":
		name_var = request.POST['name']
		email_var = request.POST['email']
		subject_var = request.POST['subject']
		message_var = request.POST['message']
		
		send_mail(
			subject_var,
			message_var,
			email_var,
			['shivampawar515@gmail.com'],
		)

		return render(request,'contact.html',{'name_var':name_var})


	else:
		return render(request,'contact.html',{})	

class Hotels(View):

	template_name = 'destination.html'

	def displayHotel(self, request, *args, **kwargs):
		ht = Hotel.objects.all() 

		return render(request,self.template_name,{'ht': ht})

def destination(request):

	ht = Hotel.objects.all() 

	return render(request,'destination.html',{'ht': ht})


class Room_Status(View):

	def displayRoomDetails(self, request, *args, **kwargs):

		return render(request,'about.html',{})	

def about(request):

	return render(request,'about.html',{})	


def report(request):

	return render(request,'report.html',{})

	