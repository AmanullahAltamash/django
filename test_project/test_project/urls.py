from django.contrib import admin
from django.urls import path
from django.urls import path, include
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("<h1>Hello World</h1>")

# def user(request, pk):
#     return HttpResponse("Welcome to my website " + str(pk))



urlpatterns = [
    path('admin/', admin.site.urls),
    # path("page1/", home, name="first"),
    # path("page2/<str:pk>/", user, name="second"),
    path("", include("test_app.urls"))
]
