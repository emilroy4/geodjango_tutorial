from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Event
import calendar

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_types'] = Event.objects.values_list('event_type', flat=True).distinct()
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
    Custom Login View
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect("event_list")  # Redirect to events page
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "events/auth_form.html", {"form_type": "login"})

def register(request):
    """
    Custom Register View
    """
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
            login(request, user)  # Log in the user after successful registration
            messages.success(request, f"Account created successfully! Welcome, {username}!")
            return redirect("event_list")  # Redirect to events page

    return render(request, "events/auth_form.html", {"form_type": "register"})

def logout_user(request):
    """
    Logs out the user and redirects to the login page.
    """
    logout(request)
    return redirect("login")  # Redirect to login page after logout
