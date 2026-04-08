from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeCareProfileUpdateView, HomeCareSignupView, sair

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', sair, name='logout'),
    path('signup/', HomeCareSignupView.as_view(), name='signup'),
    path('homecare/', HomeCareProfileUpdateView.as_view(), name='homecare_profile'),
]
