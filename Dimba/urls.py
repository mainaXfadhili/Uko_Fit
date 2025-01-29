from django.urls import path
from . import views

app_name = 'Dimba'

urlpatterns = [
    path('', views.home, name='home'),
    path('community/', views.community, name='community'),
    path('resources/', views.resources, name='resources'),
    path('location/', views.location, name='location'),
    path('workout/', views.workout, name='workout'),
    path('mealplanning/', views.mealplanning, name='mealplanning'),
    path('contact/', views.contact, name='contact'),
    path('nutritioncalculator/', views.nutritioncalculator, name='nutritioncalculator'),
    path('join-group/<int:group_id>/', views.join_group, name='join_group'),
    path('create_group/', views.create_group, name='create_group'),
    path('meditation/', views.meditation, name='meditation'),
    path('save-diary-entry/', views.save_diary_entry, name='save_diary_entry'),
    path('videos/', views.videos, name='videos'),
    # path('booking-confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('save-contact/', views.save_contact, name='save_contact'),
]

print("URL patterns:", urlpatterns)

