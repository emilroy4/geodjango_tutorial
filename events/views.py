from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Event
import calendar

# Event views
class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'  # Template for event listing
    context_object_name = 'events'
    ordering = ['start_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_types'] = Event.objects.values_list('event_type', flat=True).distinct()
        context['months'] = [(i, calendar.month_name[i]) for i in range(1, 13)]
        years = Event.objects.values_list('start_date__year', flat=True).distinct().order_by('-start_date__year')
        context['years'] = years
        return context

# Default home page view
def home(request):
    return render(request, 'home.html')  # Simple homepage for `/`

# Custom login view
def custom_login(request):
    if request.user.is_authenticated:
        return redirect("event_list")  # Redirect authenticated users to events

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("event_list")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "events/auth_form.html", {"form_type": "login"})

# Register view
def register(request):
    if request.user.is_authenticated:
        return redirect("event_list")

    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            login(request, user)
            return redirect("event_list")

    return render(request, "events/auth_form.html", {"form_type": "register"})

# Custom logout view
def custom_logout(request):
    logout(request)
    return redirect("login")
