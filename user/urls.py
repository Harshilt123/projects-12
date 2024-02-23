from django.urls import path
from . import views

app_name = 'user'  # Namespace for your app

urlpatterns = [
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("dashboard/", views.UserDashboardView.as_view(), name="dashboard"),
    # path("developer_dashboard/", views.DeveloperDashboardView.as_view(), name="developer_dashboard"),
    path("logout/", views.LogoutView.as_view(), name="logout"),  # Using Django's built-in LogoutView
]
