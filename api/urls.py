from django.urls import path
from . import views
from .views import LeadCreateView

urlpatterns = [
    path('', views.index, name='index'), 
    path('leads/dashboard/', views.lead_dashboard, name='lead_dashboard'),
    path('leads/create/', views.create_lead, name='create_lead'),  # Old view for local testing
    path('api/leads/create/', LeadCreateView.as_view(), name='api_create_lead'),  # New API endpoint
]