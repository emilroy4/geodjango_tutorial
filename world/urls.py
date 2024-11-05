from django.urls import path
from .views import home  # Import the view you created

urlpatterns = [
    path('', home, name='home'),  # Route for the home page
]

