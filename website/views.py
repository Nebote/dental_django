from django.shortcuts import render
from django.core.mail import send_mail

def doma(request):
	return render(request, 'doma.html', {})

def za_nas(request):
	return render(request, 'za_nas.html', {})

def novosti_promocii(request):
	return render(request, 'novosti_promocii.html', {})


def blogdetails(request):
	return render(request, 'blogdetails.html', {})


def cenovnik(request):
	return render(request, 'cenovnik.html', {})


def uslugi(request):
	return render(request, 'uslugi.html', {})





def kontakt(request):
	if request.method == "POST":
		#do stuff
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']


		send_mail(
			message_name,
			message,
			message_email,
			['nebojshastojanoski@gmail.com'],
			fail_silently=False,
			)


		return render(request, 'kontakt.html', {'message_name': message_name})

	else:
		# return the page
		return render(request, 'kontakt.html', {})


#english

def home(request):
	return render(request, 'english/home.html', {})

def service(request):
	return render(request, 'english/service.html', {})

def about(request):
	return render(request, 'english/about.html', {})


def pricing(request):
	return render(request, 'english/pricing.html', {})


def blog(request):
	return render(request, 'english/blog.html', {})





def contact(request):
	if request.method == "POST":
		#do stuff
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']


		send_mail(
			message_name,
			message,
			message_email,
			['nebojshastojanoski@gmail.com'],
			fail_silently=False,
			)


		return render(request, 'english/contact.html', {'message_name': message_name})

	else:
		# return the page
		return render(request, 'english/contact.html', {})



	#albanian

		
def shtepi(request):
	return render(request, 'shqip/shtepi.html', {})

def rreth_nesh(request):
	return render(request, 'shqip/rreth_nesh.html', {})

def sherbimet(request):
	return render(request, 'shqip/sherbimet.html', {})	

def cmimeve(request):
	return render(request, 'shqip/cmimeve.html', {})	

def lajmedhepromovime(request):
	return render(request, 'shqip/lajmedhepromovime.html', {})

def kontaktsq(request):
	return render(request, 'shqip/kontakt.html', {})


