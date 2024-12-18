"""
URL configuration for geodjango_tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from events import views as event_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", event_views.home, name="home"),  # Root URL
    path("events/", include("events.urls")),

    # Authentication URLs
    path("login/", event_views.custom_login, name="login"),
    path("register/", event_views.register, name="register"),
    path("logout/", event_views.custom_logout, name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



