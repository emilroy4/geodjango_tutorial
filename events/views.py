from django.views.generic import ListView, DetailView
from .models import Event
import calendar

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime


# Event List View
class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'  # Updated to match your template path
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

        # Debug print
        print(f"Events count: {self.get_queryset().count()}")
        print(f"Event types: {list(context['event_types'])}")
        print(f"Years: {list(years)}")

        return context

# Event Detail View
class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'  # Update to your template path


# Login View
def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("event_list")  # Redirect to event list
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "auth_form.html", {"form": form, "title": "Login"})

# Register View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "auth_form.html", {"form": form, "title": "Register"})

# Logout View
def custom_logout(request):
    logout(request)
    return redirect("login")
