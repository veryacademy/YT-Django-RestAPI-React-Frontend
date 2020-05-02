from django.urls import path
from . import views

urlpatterns = [
    path('events/api/', views.LeadListCreate.as_view()),
]