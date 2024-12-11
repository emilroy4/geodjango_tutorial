from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.EventListView.as_view(), name='event_list'),  # Example view
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),  # Example detail view
] 
