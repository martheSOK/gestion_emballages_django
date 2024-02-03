from django.urls import path
from . import views
app_name='afrikpros'




urlpatterns = [
       path('', views.dashboard, name='dashboard'),
       path('add_depot/', views.add_depot, name='add_depot'),
       # path('liste_depot/', views.liste_depot, name='liste_depot'),
]
