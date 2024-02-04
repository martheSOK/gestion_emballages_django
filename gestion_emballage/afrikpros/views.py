from django.shortcuts import render, redirect, get_object_or_404
from .forms import *

# Create your views here.

def dashboard(request):
    return render(request,"dashboard/index.html", locals())




   
def liste_depot(request):
    listedepot=Depot.objects.all()
    return render( request,"depot/liste_depot.html",locals())






def liste_depot(request, depot_id=None):
    if depot_id:
        # Update existing depot
        depot = get_object_or_404(Depot, pk=depot_id)
        if request.method == "POST":
            form = DepotForm(request.POST, instance=depot)
            if form.is_valid():
                form.save()
                return redirect("afrikpros:liste_depot")
        else:
            form = DepotForm(instance=depot)
    else:
        # Add new depot
        if request.method == "POST":
            form = DepotForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("afrikpros:liste_depot")
        else:
            form = DepotForm()

    listedepot = Depot.objects.all()
    return render(request, "depot/liste_depot.html", {"form": form, "listedepot": listedepot})

def delete_depot(request, depot_id):
    depot = Depot.objects.get(pk=depot_id)
    depot.delete()    
    return redirect("afrikpros:liste_depot")


