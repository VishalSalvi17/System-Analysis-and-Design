from django.shortcuts import render
from django.core.mail import send_mail
from .models import Location

def home(request):

	loc1 = Location()
	loc1.id = 1
	loc1.imgss = 'gateway3.jpg'
	loc1.price = '$50/person'
	loc1.day = '1 Day Tour'
	loc1.name = 'Gateway of India'
	loc1.address = 'Mumbai, India'	

	loc2 = Location()
	loc2.id = 2
	loc2.imgss = 'hajiali.jpg'
	loc2.price = '$50/person'
	loc2.day = '1 Day Tour'
	loc2.name = 'Haji Ali Dargah'
	loc2.address = 'Mumbai, India'

	loc3 = Location()
	loc3.id = 3
	loc3.imgss = 'ew1.jpg'
	loc3.price = '$70/person'
	loc3.day = '1 Day Tour'
	loc3.name = 'Essel World'
	loc3.address = 'Mumbai, India'

	loc4 = Location()
	loc4.id = 4
	loc4.imgss = 'sg.jpg'
	loc4.price = '$60/person'
	loc4.day = '1 Day Tour'
	loc4.name = 'National Park'
	loc4.address = 'Mumbai, India'

	loc5 = Location()
	loc5.id = 5
	loc5.imgss = 'marines.jpg'
	loc5.price = '$30/person'
	loc5.day = '1 Day Tour'
	loc5.name = 'Marine Lines'
	loc5.address = 'Mumbai, India'

	loc6 = Location()
	loc6.id = 6
	loc6.imgss = 'pagoda.jpg'
	loc6.price = '$100/person'
	loc6.day = '1 Day Tour'
	loc6.name = 'Pagoda'
	loc6.address = 'Mumbai, India'

	locs=[loc1,loc2,loc3,loc4,loc5,loc6]


	return render(request,'home.html',{'loc2': loc2})

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

def destination(request):
	return render(request,'destination.html',{})

def about(request):
	return render(request,'about.html',{})	