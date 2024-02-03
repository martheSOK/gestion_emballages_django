from django.shortcuts import render, redirect
from .forms import *
# Create your views here.

def dashboard(request):
    return render(request,"dashboard/index.html", locals())



def add_depot(request):
    print("::::::::::add_depot:::::::::::::::::::")
    if request.method == "POST":
        form = DepotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("afrikpros:liste_depot")
    else:
        
        form = DepotForm()
    print(form)
    return render(request, "depot/add_depot.html", locals()) 
   
   
def liste_depot(request):
    listedepot=Depot.objects.all()
    return render( request,"depot/liste_depot.html",locals())