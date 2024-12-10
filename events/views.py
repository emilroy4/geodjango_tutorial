from django.views.generic import ListView, DetailView
from .models import Event
import calendar
from datetime import datetime

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

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'  # Update to your template path

