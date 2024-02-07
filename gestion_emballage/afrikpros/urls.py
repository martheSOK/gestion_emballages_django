from django.urls import path
from . import views
app_name='afrikpros'




urlpatterns = [
       path('', views.dashboard, name='dashboard'),
       # path('liste_depot/', views.liste_depot, name='add_depot'),
#        path('update_depot/<int:depot_id>/', views.update_depot, name='update_depot'),
       path('liste_depot/', views.liste_depot, name='liste_depot'),

    # URL for updating an existing depot
    path('liste_depot/<int:depot_id>/',  views.liste_depot, name='update_depot'),
    path('delete_depot/<int:depot_id>/',  views.delete_depot, name='delete_depot'),
    
    
    path('liste_embalage/', views.liste_embalage, name='liste_embalage'),
    
     path('manage_embalage/', views.manage_embalage, name='liste_embalage'),
     
      path('delete_embalage/<int:embalage_id>/',  views.delete_embalage, name='delete_embalage'),
    
 ]


