from django.urls import path
from . import views



urlpatterns = [
    path("",views.home, name="first"),
    path("page2/<str:pk>/", views.user, name="second"),
]
