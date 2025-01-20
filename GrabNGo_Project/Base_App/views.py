from django.shortcuts import render, redirect
from django.http import HttpResponse
from Base_App.models import BookTable, AboutUs, Feedback, ItemList, Items
from Base_App.models import BookTable
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BookTable
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# Create your views here.

def HomeView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    return render(request, 'home.html', {'items': items, 'list': list, 'review': review})

def AboutView(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html', {'data': data})


def MenuView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html', {'items': items, 'list': list})




def BookTableView(request):
    if not request.user.is_authenticated:
        # If the user is not authenticated, show an alert message
        messages.warning(request, 'You need to log in first to book a table.')
        return render(request, 'book_table.html')

    if request.method == 'POST':
        phone_number = request.POST['Phone_number']
        Email = request.POST['Email']
        Total_person = request.POST['Total_person']
        booking_data = request.POST['booking_data']

        if not phone_number or not Email or not Total_person or not booking_data:
            error_message = 'Please fill in all fields.'
            return render(request, 'book_table.html', {'error_message': error_message})

        # Create a new booking and associate it with the logged-in user
        booking = BookTable(
            user=request.user,  # Automatically set the logged-in user
            Phone_number=phone_number,
            Email=Email,
            Total_person=Total_person,
            booking_data=booking_data
        )
        booking.save()
        messages.success(request, 'Your booking has been successfully made!')
        return redirect('dashboard')  # Redirect to the dashboard after saving the booking

    return render(request, 'book_table.html')

def book_table_redirect(request):
    messages.warning(request, "You need to login to book a table.")
    return redirect('login')  # Redirecting to login page


def FeedbackView(request):
    return render(request, 'feedback.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    bookings = user.bookings.all()  # Use 'bookings' instead of 'booking_set'
    return render(request, 'dashboard.html', {'bookings': bookings})

def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Ensure 'dashboard' is correctly mapped in urls.py
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

def LogoutView(request):
    logout(request)  # Logs the user out
    return redirect('Home')  # Redirects to the home page