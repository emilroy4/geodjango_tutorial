from django.views.generic import ListView, DetailView
from .models import Event  # Import your Event model

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'  # Update to your template path
    context_object_name = 'events'  # Specify the context variable name

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Add additional context if needed
        return context

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'  # Update to your template path

