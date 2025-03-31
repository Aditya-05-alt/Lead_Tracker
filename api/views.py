from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializer import LeadSerializer
from .models import Lead
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from rest_framework import status

# Index View (Render your main page)
def index(request):
    return render(request, 'api/index.html')


# Lead Dashboard View (Display Leads with Filtering)
def lead_dashboard(request):
    leads = Lead.objects.all().order_by('-created_at')  # Display newest leads first

    # Filtering
    status_filter = request.GET.get('status')
    source = request.GET.get('source')
    medium = request.GET.get('medium')
    search_query = request.GET.get('search')

    if status_filter and status_filter != 'All':
        leads = leads.filter(status=status_filter)
    if source and source != 'All':
        leads = leads.filter(source=source)
    if medium and medium != 'All':
        leads = leads.filter(medium=medium)
    if search_query:
        leads = leads.filter(name__icontains=search_query)

    context = {
        'leads': leads,
        'selected_status': status_filter,
        'selected_source': source,
        'selected_medium': medium,
        'search_query': search_query
    }
    return render(request, 'api/lead_dashboard.html', context)


# ✅ Class-Based View for Lead Capture (Preferred for APIs)
@method_decorator(csrf_exempt, name='dispatch')  # Allow cross-origin JS without CSRF
class LeadCreateView(APIView):

    def post(self, request):
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Lead captured successfully."}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
