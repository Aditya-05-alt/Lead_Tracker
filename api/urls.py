from django.urls import path
from . import views
from .views import LeadCreateView

urlpatterns = [
    path('', views.index, name='index'), 
    path('leads/dashboard/', views.lead_dashboard, name='lead_dashboard'), 
    path('leads/create/', LeadCreateView.as_view(), name='create_lead'),
]