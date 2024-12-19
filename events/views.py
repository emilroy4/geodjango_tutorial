from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Event
import calendar
import math

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points 
    on the Earth's surface specified in decimal degrees.
    Returns distance in kilometers.
    """
    R = 6371  # Radius of Earth in kilometers
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def home(request):
    """
    Home View - Redirect to login/register if not authenticated, else redirect to events.
    """
    if request.user.is_authenticated and request.user.is_active:
        return redirect("event_list")
    return render(request, "events/auth_form.html", {"form_type": "login"})

class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'
    ordering = ['start_date']
    login_url = '/login/'  # Redirect unauthenticated users to login
    redirect_field_name = 'next'

    def get_queryset(self):
        queryset = super().get_queryset()
        user_location = self.request.GET.get('location', None)

        if user_location:
            try:
                user_lat, user_lng = map(float, user_location.split(','))
                # Add distance to each event and filter within 10 km
                events_with_distance = []
                for event in queryset:
                    event_distance = haversine(user_lat, user_lng, event.latitude, event.longitude)
                    if event_distance <= 10:  # Within 10 km
                        event.distance = event_distance
                        events_with_distance.append(event)

                # Sort by distance
                events_with_distance.sort(key=lambda x: x.distance)
                return events_with_distance
            except ValueError:
                pass  # Ignore invalid coordinates

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_types'] = Event.objects.values_list('event_type', flat=True).distinct().order_by('event_type')
        context['months'] = [(i, calendar.month_name[i]) for i in range(1, 13)]
        years = Event.objects.values_list('start_date__year', flat=True).distinct().order_by('-start_date__year')
        context['years'] = years
        return context

class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    login_url = '/login/'  # Redirect unauthenticated users to login
    redirect_field_name = 'next'

def custom_login(request):
    """
    Custom Login View with error feedback only.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("event_list")  # Redirect to events page
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, "events/auth_form.html", {"form_type": "login"})

def register(request):
    """
    Custom Register View with real-time feedback for errors.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Validate user inputs
        if not username or not password1 or not password2:
            messages.error(request, "All fields are required.")
        elif len(password1) < 6:
            messages.error(request, "Password must be at least 6 characters long.")
        elif password1 != password2:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different one.")
        else:
            # Create user
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            login(request, user)  # Log in the user after successful registration
            return redirect("event_list")  # Redirect to events page

    return render(request, "events/auth_form.html", {"form_type": "register"})

def logout_user(request):
    """
    Logs out the user and redirects to the login page.
    """
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("login")
