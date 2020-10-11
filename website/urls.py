from django.urls import path
from . import views

urlpatterns = [
	path('', views.doma, name="doma"),
	path('kontakt', views.kontakt, name="kontakt"),
	path('za_nas', views.za_nas, name="za_nas"),
	path('novosti_promocii', views.novosti_promocii, name="novosti_promocii"),
	path('blogdetails', views.blogdetails, name="blogdetails"),
	path('cenovnik', views.cenovnik, name="cenovnik"),
	path('uslugi', views.uslugi, name="uslugi"),
	path('english/home', views.home, name="home"),

	#english
	path('english/about', views.about, name="about"),
	path('english/service', views.service, name="service"),
	path('english/pricing', views.pricing, name="pricing"),
	path('english/blog', views.blog, name="blog"),
    path('english/contact', views.contact, name="contact"),

    #albanian
    path('shqip/shtepi', views.shtepi, name="shtepi"),
    path('shqip/sherbimet', views.sherbimet, name="sherbimet"),
    path('shqip/rreth_nesh', views.rreth_nesh, name="rreth_nesh"),
    path('shqip/cmimeve', views.cmimeve, name="cmimeve"),
    path('shqip/lajmedhepromovime', views.lajmedhepromovime, name="lajmedhepromovime"),
    path('shqip/kontaktsq', views.kontaktsq, name="kontaktsq"),

   




    

]
