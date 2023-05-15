from . import views
from django.urls import path

urlpatterns = [

    path('adventure',views.adventure,name='adventure'),
    path('princesses',views.princesses,name='princesses'),
    path('magazine',views.magazine,name='magazine'),


]
