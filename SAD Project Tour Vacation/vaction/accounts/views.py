from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from website.models import Location, Hotel
from django.views.generic import View 

class Users(View):

	def registrationDetails(self, request, *args, **kwargs):
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		psw = request.POST['psw'] 
		psw_repeat = request.POST['psw_repeat']

		if psw == psw_repeat:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username Already Taken')
				return redirect('register')

			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email_id already exists')
				return redirect('register')

			else:	
				user = User.objects.create_user(username = username, password = psw, email= email, first_name = first_name, last_name = last_name) 
				user.save();
				return redirect('login')
		else:
			messages.info(request,'Password is not matching.')
			return redirect('register')

		return redirect('/')	

	def loginDetails(self, request, *args, **kwargs):

		username = request.POST['username']
		psw = request.POST['psw']

		user = auth.authenticate(username=username, password=psw)

		if user is not None:
			auth.login(request,user)
			return redirect('payment')
				
		else:
			messages.info(request,'Invalid Credentials')
			return redirect('login')

	def logout(self, request, *args, **kwargs):
		auth.logout(request)
		return redirect('/')



def register(request):
	if request.method == "POST":
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		psw = request.POST['psw'] 
		psw_repeat = request.POST['psw_repeat']

		if psw == psw_repeat:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username Already Taken')
				return redirect('register')

			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email_id already exists')
				return redirect('register')

			else:	
				user = User.objects.create_user(username = username, password = psw, email= email, first_name = first_name, last_name = last_name) 
				user.save();
				return redirect('login')
		else:
			messages.info(request,'Password is not matching.')
			return redirect('register')

		return redirect('/')

	else:	
		return render(request,'register.html')

def login(request):
	if request.method == "POST":

		username = request.POST['username']
		psw = request.POST['psw']

		user = auth.authenticate(username=username, password=psw)

		if user is not None:
			auth.login(request,user)
			return redirect('payment')
				
		else:
			messages.info(request,'Invalid Credentials')
			return redirect('login')

	else:	
		return render(request,'login.html')	



def logout(request):	
	auth.logout(request)
	return redirect('/')

class Make_Payment(View):

	def paymentDetails(self, request, *args, **kwargs):
		fname = request.POST.get('fullname')
		email = request.POST.get('email')
		City = request.POST.get('city')
		State = request.POST.get('state')
		Zip = request.POST.get('zip')
		Name_on_card = request.POST.get('cardname')
		expiry_month = request.POST.get('expmonth')
		expiry_year = request.POST.get('expyear')
		CVV = request.POST.get('cvv') 
		return render(request,'report.html',{'fname':fname})


def payment(request):

	if request.method == "POST":
		fname = request.POST.get('fullname')
		return render(request,'report.html',{'fname': fname})
	
	else:
			
		return render(request,'payment.html',{})