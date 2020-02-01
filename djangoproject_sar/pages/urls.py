from django.urls import path
from . import views 

urlpatterns = [  
	path('',views.home,name='home'), 
	path('about/',views.about,name='about'), 
	path('contacts/',views.contacts,name='contacts'),
    path('testimonials/',views.testimonials ,name='testimonials'),
    path('contact/',views.contact,name='contact'),  
    path('result1/',views.result1,name='result1'), 
    path('result2/',views.result2,name='result2'), 
    path('result3/',views.result3,name='result3'), 
    path('result4/',views.result4,name='result4'),
    path('gallery/',views.gallery,name='gallery'),
    path('admission/',views.admission,name='admission'), 
    path('form/',views.form,name='form'),
 ] 



