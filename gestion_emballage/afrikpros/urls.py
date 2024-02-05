from django.urls import path
from . import views
app_name='afrikpros'




urlpatterns = [
    

#*********page d'accueille********
       path('', views.dashboard, name='dashboard'),
       # path('liste_depot/', views.liste_depot, name='add_depot'),
       #path('update_depot/<int:depot_id>/', views.update_depot, name='update_depot'),


#**********depot*****************
       path('liste_depot/', views.liste_depot, name='liste_depot'),

       # URL for updating an existing depot
       path('liste_depot/<int:depot_id>/',  views.liste_depot, name='update_depot'),
       path('delete_depot/<int:depot_id>/',  views.delete_depot, name='delete_depot'),



#**********fournisseur*****************
       path('liste_fournisseur/', views.liste_fournisseur, name='liste_fournisseur'),

       # URL for updating an existing fournisseur
       path('liste_fournisseur/<int:fournisseur_id>/',  views.liste_fournisseur, name='update_fournisseur'),
       path('delete_fournisseur/<int:fournisseur_id>/',  views.delete_fournisseur, name='delete_fournisseur'),

     
 


#**********user*****************
       path('liste_users/', views.liste_users, name='liste_users'),

       # URL for updating an existing user
       path('liste_users/<int:user_id>/',  views.liste_users, name='update_user'),
       path('delete_user/<int:user_id>/',  views.delete_user, name='delete_user'),

     
 ]


