from django.shortcuts import render

def home(request): 
	return render(request,"home.html",{}) 
def about(request): 
	from pages.namer import bob
	return render(request,"about.html", {"my_stuff": bob}) 
def contacts(request): 
	return render(request,"contacts.html",{})  
def testimonials(request):   
	from pages.namer import bob
	return render(request,"testimonials.html",{"my_stuff": bob()})    
def contact(request):  
	from pages.namer import bob
	return render(request,"contact.html",{"my_stuff": bob()}) 
def result1(request): 
	return render(request,"result1.html",{})  
def result2(request): 
	return render(request,"result2.html",{})   
def result3(request): 
	return render(request,"result3.html",{})  
def result4(request): 
	return render(request,"result4.html",{})  
def gallery(request): 
	return render(request,"gallery.html",{})  
def admission(request): 
	return render(request,"admission.html",{})  
def form(request): 
	return render(request,"form.html",{}) 