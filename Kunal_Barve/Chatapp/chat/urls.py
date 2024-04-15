from django.urls import path
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", chat_views.chatPage, name="chat-page"),

    # Login and logout URLs
    path("auth/login/", LoginView.as_view(template_name="LoginPage.html"), name="login-user"),
    path("logout/", LogoutView.as_view(next_page="login-user"), name="logout-user"),
        path('check-session-expiration/', chat_views.check_session_expiration),

]
