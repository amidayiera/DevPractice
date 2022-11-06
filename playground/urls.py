from django.urls import path
from . import views

# URLConf - each app can have its own
urlpatterns = [
    path('hello/', views.say_hello)
]
