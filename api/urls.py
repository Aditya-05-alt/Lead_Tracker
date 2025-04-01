from django.urls import path
from . import views
from .views import LeadCreateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'), 
    path('leads/dashboard/', views.lead_dashboard, name='lead_dashboard'), 
    path('leads/create/', LeadCreateView.as_view(), name='create_lead'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)