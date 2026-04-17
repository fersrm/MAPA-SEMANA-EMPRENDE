from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from MapaApp import views

urlpatterns = [
    path("", views.MapaTemplaView.as_view(), name="Mapa"),
    path("mapa_carga/", views.MapaFormView.as_view(), name="MapaCarga"),

    path(
        "login/",
        LoginView.as_view(
            template_name="pages/registration/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
]