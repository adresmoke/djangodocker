from django.urls import path, include
from . import views
from .views import SignupView
urlpatterns = [
    path('', views.public_home, name='home'),
    path('register/', SignupView.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls'))
    ]


