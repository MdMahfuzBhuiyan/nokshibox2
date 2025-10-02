from django.shortcuts import redirect
from django.urls import reverse

class AdminRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If superuser is logged in and not already at dashboard → redirect
        if request.user.is_authenticated and request.user.is_superuser:
            dashboard_url = reverse('admin_dashboard')
            if not request.path.startswith(dashboard_url) and not request.path.startswith('/logout/'):
                return redirect(dashboard_url)
        return self.get_response(request)
