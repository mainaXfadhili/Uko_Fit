from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Group, Turf, Booking
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta

def home(request):
    """View function for the home page"""
    turfs = Turf.objects.all()
    return render(request, 'index.html', {'turfs': turfs})

def community(request):
    """View function for the community page"""
    groups = Group.objects.all().prefetch_related('members')
    return render(request, 'community.html', {'groups': groups})

@login_required
def create_group(request):
    """View function to create a new group"""
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            description = request.POST.get('description')
            
            if not name or not description:
                messages.error(request, 'Both name and description are required.')
                return redirect('Dimba:community')
            
            group = Group.objects.create(
                name=name,
                description=description,
                created_by=request.user
            )
            group.members.add(request.user)
            
            messages.success(request, 'Group created successfully!')
            return redirect('Dimba:community')
        except Exception as e:
            messages.error(request, f'Error creating group: {str(e)}')
            return redirect('Dimba:community')
    
    return redirect('Dimba:community')

@login_required
def book_turf(request, turf_id):
    turf = get_object_or_404(Turf, id=turf_id)
    
    if request.method == 'POST':
        try:
            booking_date = request.POST.get('booking_date')
            start_time = request.POST.get('start_time')
            hours = int(request.POST.get('hours'))

            total_price = turf.price_per_hour * hours

            booking = Booking.objects.create(
                user=request.user,
                turf=turf,
                booking_date=booking_date,
                start_time=start_time,
                hours=hours,
                total_price=total_price,
                status='PENDING'
            )

            return redirect('Dimba:payment', booking_id=booking.id)

        except Exception as e:
            messages.error(request, f"Booking failed: {str(e)}")
            return redirect('Dimba:book_turf', turf_id=turf_id)

    context = {
        'turf': turf,
        'min_date': datetime.now().date(),
        'max_date': (datetime.now() + timedelta(days=30)).date(),
    }
    return render(request, 'book_turf.html', context)

@login_required
def payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        try:
            booking.status = 'CONFIRMED'
            booking.payment_completed = True
            booking.save()
            
            messages.success(request, "Payment successful! Your booking is confirmed.")
            return redirect('Dimba:booking_confirmation', booking_id=booking.id)
            
        except Exception as e:
            messages.error(request, f"Payment failed: {str(e)}")
    
    return render(request, 'payment.html', {'booking': booking})

@login_required
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    return render(request, 'booking_confirmation.html', {'booking': booking})

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
    turfs = Turf.objects.all()
    return render(request, 'location.html', {'turfs': turfs})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Dimba:home')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('Dimba:home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('Dimba:home')
        else:
            messages.error(request, "Registration failed. Please correct the errors.")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def resources(request):
    return render(request, 'resources.html')

