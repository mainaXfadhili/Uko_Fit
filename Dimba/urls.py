from django.urls import path
from . import views

app_name = 'Dimba'

urlpatterns = [
    path('', views.home, name='home'),
    path('community/', views.community, name='community'),
    path('resources/', views.resources, name='resources'),
    path('location/', views.location, name='location'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logout_view, name='logout'),
    path('join-group/<int:group_id>/', views.join_group, name='join_group'),
    path('create_group/', views.create_group, name='create_group'),
    path('register/', views.register, name='register'),
    # path('book-turf/<int:turf_id>/', views.book_turf, name='book_turf'),
    # path('payment/<int:booking_id>/', views.payment, name='payment'),
    # path('booking-confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('save-contact/', views.save_contact, name='save_contact'),
]

print("URL patterns:", urlpatterns)

