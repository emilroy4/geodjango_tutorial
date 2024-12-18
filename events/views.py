from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Event
import calendar

import os
print("Looking for template at:", os.path.abspath('templates/auth_form.html'))


class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'  # Template for event listing
    context_object_name = 'events'
    ordering = ['start_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add filter data to context
        context['event_types'] = Event.objects.values_list('event_type', flat=True).distinct()
        context['months'] = [(i, calendar.month_name[i]) for i in range(1, 13)]
        
        # Get years from start_date instead of using dates()
        years = Event.objects.values_list('start_date__year', flat=True).distinct().order_by('-start_date__year')
        context['years'] = years

        return context

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'  # Template for event detail view


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
            return redirect("event_list")  # Redirect to event list on success
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "auth_form.html", {"form_type": "login"})


def register(request):
    """
    Custom Register View
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match")
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                login(request, user)  # Log in the user after successful registration
                return redirect("event_list")  # Redirect to event list

    return render(request, "auth_form.html", {"form_type": "register"})


def custom_logout(request):
    """
    Custom Logout View
    """
    logout(request)
    return redirect("login")  # Redirect to login page after logging out
