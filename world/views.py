from django.shortcuts import redirect, render

def homepage(request):
    """
    Redirect authenticated users to events list.
    Show login/register page for unauthenticated users.
    """
    if request.user.is_authenticated:
        return redirect("event_list")  # Redirect to events page
    else:
        return render(request, "world/homepage.html")  # Show custom homepage
