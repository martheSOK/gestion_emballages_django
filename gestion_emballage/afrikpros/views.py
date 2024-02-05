from django.shortcuts import render, redirect, get_object_or_404
from .forms import *

# Create your views here.

def dashboard(request):
    return render(request,"dashboard/index.html", locals())



#**********CRUD for DEPOT****************


 #***********read(affichage)***********
def liste_depot(request):
    listedepot=Depot.objects.all()
    return render( request,"depot/liste_depot.html",locals())



#***********create or update**************
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


#*********supresssion***********
def delete_depot(request, depot_id):
    depot = Depot.objects.get(pk=depot_id)
    depot.delete()    
    return redirect("afrikpros:liste_depot")






#**********CRUD for FORUNISSEUR****************

#******read********
def liste_fournisseur(request):
    listefournisseur=Fournisseur.objects.all()
    return render( request,"fournisseur/liste_fournisseur.html",locals())



def liste_fournisseur(request, fournisseur_id=None):
    if fournisseur_id:
        # update existing fournisseur
        fournisseur = get_object_or_404(Fournisseur, pk=fournisseur_id)
        if request.method == "POST":
            form = FournisseurForm(request.POST, instance=fournisseur)
            if form.is_valid():
                form.save()
                return redirect("afrikpros:liste_fournisseur")
        else:
            form = FournisseurForm(instance=fournisseur)

    else:
        # Add new fournisseur
        if request.method == "POST":
            form = FournisseurForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("afrikpros:liste_fournisseur")
        else:
            form = FournisseurForm()

    listefournisseur =Fournisseur.objects.all()
    return render(request, "fournisseur/liste_fournisseur.html", {"form": form, "listefournisseur": listefournisseur})


#******read********
def delete_fournisseur(request, fournisseur_id):
    fournisseur = Fournisseur.objects.get(pk=fournisseur_id)
    fournisseur.delete()    
    return redirect("afrikpros:liste_fournisseur")





#**********CRUD for USER****************

#******read********
def liste_users(request):
    depots=Depot.objects.all()
    listeusers=User.objects.all()
    return render( request,"user/liste_users.html",locals())



def liste_users(request, user_id=None):
    if user_id:
        # update existing user
        user = get_object_or_404(Personne, pk=user_id)
        if request.method == "POST":
            form = UserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect("afrikpros:liste_users")
        else:
            form = UserForm(instance=user)

    else:
        # Add new user
        if request.method == "POST":
            form = UserForm(request.POST)
            print(form)
            if form.is_valid():
                form.save()
                return redirect("afrikpros:liste_users")
        else:
            form = UserForm()
            print(form)

    listeuser =Personne.objects.all()
    depots=Depot.objects.all()
    return render(request, "user/liste_users.html", {"form": form, "listeuser": listeuser,"depots":depots})


#******read********
def delete_user(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()    
    return redirect("afrikpros:liste_users")




