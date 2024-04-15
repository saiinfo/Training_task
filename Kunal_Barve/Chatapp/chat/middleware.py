from django.contrib.auth import logout
from django.utils import timezone
from django.shortcuts import redirect

class SessionExpirationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Get the session expiration time
            session_expiration_time = request.session.get_expiry_date()

            # Check if the session has expired
            if session_expiration_time and session_expiration_time <= timezone.now():
                # Log out the user
                logout(request)

                # Redirect to the login page or any other desired page
                return redirect('login-user')

        return response
