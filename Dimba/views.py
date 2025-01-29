from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Group, Turf #Booking
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from decimal import Decimal
from .models import Contact  # Ensure you import the Contact model
from .models import DiaryEntry


def home(request):
    """View function for the home page"""
    turfs = Turf.objects.all()
    return render(request, 'index.html', {'turfs': turfs})


def community(request):
    """View function for the community page"""
    if request.method == 'POST':
        # Handle the group creation form submission
        group_name = request.POST.get('group_name')
        location = request.POST.get('location')
        skill_level = request.POST.get('skill_level')
        description = request.POST.get('description')
        image = request.FILES.get('image')  # Get the uploaded image

        # Create the group
        group = Group.objects.create(
            name=group_name,
            location=location,
            skill_level=skill_level,
            description=description,
            image=image,
            creator=request.user
        )

        messages.success(request, 'Group created successfully!')
        return redirect('Dimba:community')  # Redirect to the same page to see the new group

    # Fetch all groups to display, ordered by created_at
    groups = Group.objects.all().order_by('-created_at')
    return render(request, 'community.html', {'groups': groups})

# @login_required
# def create_group(request):
#     """View function to create a new group"""
#     if request.method == 'POST':
#         try:
#             group = Group.objects.create(
#                 name=request.POST['name'],
#                 description=request.POST['description'],
#                 location=request.POST['location'],
#                 creator=request.user
#             )
            
#             if 'image' in request.FILES:
#                 group.image = request.FILES['image']
#                 group.save()
                
#             messages.success(request, 'Group created successfully!')
#             return redirect('Dimba:community')
#         except Exception as e:
#             messages.error(request, f'Error creating group: {str(e)}')
    
#     return redirect('Dimba:community')
@csrf_exempt
def save_contact(request):
    """View function to handle contact form submissions"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        try:
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def location(request):
    turfs = [
        {
            'id': 1,
            'name': 'Karen Road Turf',
            'address': 'Karen Road, Nairobi',
            'price': 5000,
            'opening_hours': '7:00 AM - 10:00 PM',
            'rating': 4.9,
            'facilities': ['Premium facilities', 'Club house', 'Restaurant', 'Pro shop', 'Parking'],
            'contact': '+254 777 890123',
            'image': 'images/turf1.jpg',
            'lat': -1.3089,
            'lng': 36.7372
        },
        {
            'id': 2,
            'name': 'Astro Turf Kileleshwa',
            'address': 'Kileleshwa Ring Road',
            'price': 4500,
            'opening_hours': '6:00 AM - 11:00 PM',
            'rating': 4.7,
            'facilities': ['Floodlights', 'Changing rooms', 'Parking', 'Water'],
            'contact': '+254 722 123456',
            'image': 'images/turf2.jpg',
            'lat': -1.2841,
            'lng': 36.7776
        },
        # Add 10 more turfs with realistic Nairobi locations
    ]
    return render(request, 'location.html', {'turfs': turfs})

'''def login_view(request):
    """View function for user login"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', 'Dimba:home')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')'''

'''def logout_view(request):
"""View function for user logout"""
logout(request)
messages.success(request, 'Successfully logged out!')
return redirect('Dimba:home')

def register(request):
    """View function for user registration"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('Dimba:login')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})'''

from django.shortcuts import render

def videos(request):
    """View function for the video tutorial page"""
    return render(request, 'videos.html')

@csrf_exempt
def save_diary_entry(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        entry = data.get('entry')
        if entry:
            DiaryEntry.objects.create(entry=entry)
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'No entry provided'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def resources(request):
    """View function for the resources page"""
    tutorials = [
        {
            'title': 'Advanced Dribbling Skills',
            'duration': '15 mins',
            'views': '10.5K',
            'image': 'images/a1.jpg',
            'url': '#'
        },
        {
            'title': 'Perfect Your Shot',
            'duration': '20 mins',
            'views': '8.2K',
            'image': 'images/a2.jpg',
            'url': '#'
        },
        {
            'title': 'Precision Passing',
            'duration': '18 mins',
            'views': '7.8K',
            'image': 'images/a3.jpg',
            'url': '#'
        }
    ]

    training_programs = [
        {
            'title': 'Football Fitness',
            'intensity': 'High Intensity',
            'duration': '45 mins',
            'image': 'images/a4.jpg',
            'url': '#'
        },
        {
            'title': 'Speed & Agility',
            'intensity': 'Medium Intensity',
            'duration': '30 mins',
            'image': 'images/a5.jpg',
            'url': '#'
        },
        {
            'title': 'Core Strength',
            'intensity': 'High Intensity',
            'duration': '40 mins',
            'image': 'images/a6.jpg',
            'url': '#'
        }
    ]

    books = [
        {
            'title': 'Modern Football Tactics',
            'rating': '4.8/5',
            'pages': '250',
            'image': 'images/b1.png',
            'url': '#'
        },
        {
            'title': 'Complete Coaching Guide',
            'rating': '4.9/5',
            'pages': '300',
            'image': 'images/b2.png',
            'url': '#'
        },
        {
            'title': 'Football Nutrition Guide',
            'rating': '4.7/5',
            'pages': '200',
            'image': 'images/b3.png',
            'url': '#'
        }
    ]

    context = {
        'tutorials': tutorials,
        'training_programs': training_programs,
        'books': books
    }

    return render(request, 'Dimba/resources.html', context)

#@login_required
def join_group(request, group_id):
    """View function for joining a group"""
    group = get_object_or_404(Group, id=group_id)
    
    if request.user not in group.members.all():
        group.members.add(request.user)
        messages.success(request, f'You have successfully joined {group.name}!')
    else:
        messages.info(request, f'You are already a member of {group.name}.')
    
    return redirect('Dimba:community')

#@login_required
def book_turf(request, turf_id):
    """View function for booking a turf"""
    turf = get_object_or_404(Turf, id=turf_id)
    
    if request.method == 'POST':
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        
        try:
            # Calculate duration in hours
            start = datetime.strptime(start_time, '%H:%M')
            end = datetime.strptime(end_time, '%H:%M')
            duration = (end - start).seconds / 3600
            
            # Calculate total price
            total_price = turf.price_per_hour * Decimal(str(duration))
            
            # Create booking
            booking = Booking.objects.create(
                user=request.user,
                turf=turf,
                date=date,
                start_time=start_time,
                end_time=end_time,
                total_price=total_price,
                status='pending'
            )
            
            messages.success(request, 'Booking created successfully!')
            return redirect('Dimba:booking_detail', booking_id=booking.id)
            
        except Exception as e:
            messages.error(request, f'Error creating booking: {str(e)}')
            return redirect('Dimba:turf_detail', turf_id=turf_id)
    
    context = {
        'turf': turf
    }
    
    return render(request, 'Dimba/book_turf.html', context)

def mealplanning(request):
    """View function for the meal planning page"""
    return render(request, 'mealplanning.html')

def save_diary_entry(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        entry = data.get('entry')
        if entry:
            DiaryEntry.objects.create(entry=entry)
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'No entry provided'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def nutritioncalculator(request):
    """View function for the nutrition calculator page"""
    return render(request, 'nutritioncalculator.html')

def meditation(request):
    """View function for the meditation page"""
    return render(request, 'meditation.html')

def workout(request):
    """View function for the workout page"""
    # Check if user wants to return to resources
    if request.GET.get('return_to_resources'):
        return redirect('Dimba:resources')

    workout_categories = {
        'weightLoss': {
            'cardio': ['Running', 'Cycling', 'Swimming', 'Jump Rope'],
            'strength': ['Circuit Training', 'Bodyweight Exercises', 'Light Weights'],
            'hiit': ['Burpees', 'Mountain Climbers', 'Jump Squats'],
            'yoga': ['Power Yoga', 'Vinyasa Flow', 'Hot Yoga']
        },
        'muscleGain': {
            'cardio': ['Sprint Intervals', 'Rowing', 'Stair Climbing'],
            'strength': ['Heavy Weight Training', 'Compound Exercises', 'Progressive Overload'],
            'hiit': ['Weighted HIIT', 'Resistance Training', 'Tabata'],
            'yoga': ['Power Yoga', 'Strength-Based Yoga', 'Core Power']
        },
        'endurance': {
            'cardio': ['Long Distance Running', 'Cycling', 'Swimming'],
            'strength': ['Endurance Training', 'Circuit Training', 'Light Weights'],
            'hiit': ['Endurance HIIT', 'Cardio Intervals', 'Stamina Building'],
            'yoga': ['Flow Yoga', 'Continuous Movement', 'Dynamic Stretching']
        },
        'flexibility': {
            'cardio': ['Dynamic Stretching', 'Light Cardio', 'Mobility Work'],
            'strength': ['Dynamic Flexibility', 'Mobility Training', 'Stretching'],
            'hiit': ['Mobility HIIT', 'Dynamic Movement', 'Flow Sequences'],
            'yoga': ['Yin Yoga', 'Deep Stretching', 'Flexibility Flow']
        }
    }

    context = {
        'workout_categories': workout_categories,
        'goals': ['weightLoss', 'muscleGain', 'endurance', 'flexibility'],
        'workout_types': ['cardio', 'strength', 'hiit', 'yoga']
    }

    return render(request, 'workout.html', context)

#@login_required
def payment(request, booking_id):
    """View function for handling payments"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        
        try:
            # Update booking status
            booking.status = 'paid'
            booking.payment_method = payment_method
            booking.payment_date = datetime.now()
            booking.save()
            
            # Send confirmation email (you can implement this later)
            # send_booking_confirmation_email(booking)
            
            messages.success(request, 'Payment successful! Your booking is confirmed.')
            return redirect('Dimba:booking_detail', booking_id=booking.id)
            
        except Exception as e:
            messages.error(request, f'Payment failed: {str(e)}')
            return redirect('Dimba:payment', booking_id=booking.id)
    
    context = {
        'booking': booking,
        'payment_methods': [
            {
                'id': 'mpesa',
                'name': 'M-PESA',
                'icon': 'images/mpesa-logo.png'
            },
            {
                'id': 'card',
                'name': 'Credit/Debit Card',
                'icon': 'images/card-icon.png'
            }
        ]
    }
    
    return render(request, 'Dimba/payment.html', context)

#@login_required
def booking_confirmation(request, booking_id):
    """View function for displaying booking confirmation"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    context = {
        'booking': booking,
        'turf': booking.turf,
        'user': request.user,
        'payment_details': {
            'amount': booking.total_price,
            'payment_method': booking.payment_method,
            'payment_date': booking.payment_date,
            'booking_reference': f'BD{booking.id:06d}'  # Creates a 6-digit booking reference
        }
    }
    
    return render(request, 'Dimba/booking_confirmation.html', context)

def resources(request):
    """View function for the resources page"""
    return render(request, 'resources.html')  # Re

# @login_required
# def community(request):
#     groups = Group.objects.all().order_by('-created_at')
#     return render(request, 'community.html', {'groups': groups})

#@login_required
def create_group(request):
    if request.method == 'POST':
        group = Group.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            location=request.POST['location'],
            level=request.POST['level'],
            image=request.FILES['image'],
            creator=request.user
        )
        group.members.add(request.user)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

#@login_required
def join_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    group.members.add(request.user)
    return JsonResponse({'success': True})

#@login_required
def leave_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    group.members.remove(request.user)
    return JsonResponse({'success': True})

#@login_required
def delete_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.user == group.creator:
        group.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def contact(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            
            # Print the data for debugging
            print(f"Received data: Name={name}, Email={email}, Subject={subject}, Message={message}")
            
            # Create new Contact object
            contact = Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            
            print(f"Contact object created with ID: {contact.id}")
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')  # Redirect to the index page or wherever you want
            
        except Exception as e:
            print(f"Error: {str(e)}")
            messages.error(request, 'There was an error sending your message.')
            return render(request, 'index.html')  # Render the same page with an error message
            
    return render(request, 'index.html')  # Render the contact form page