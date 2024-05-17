from django.urls import path
from . import views

urlpatterns = [
    path('', views.event, name="event"),
    path('add_activity/', views.add_activity, name="add_activity")
]
