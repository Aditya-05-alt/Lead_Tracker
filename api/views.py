from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializer import LeadSerializer
from .models import Lead
import json
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

    # Apply filtering if provided in the URL parameters
    status = request.GET.get('status')
    source = request.GET.get('source')
    medium = request.GET.get('medium')
    search_query = request.GET.get('search')

    if status and status != 'All':
        leads = leads.filter(status=status)
    if source and source != 'All':
        leads = leads.filter(source=source)
    if medium and medium != 'All':
        leads = leads.filter(medium=medium)
    if search_query:
        leads = leads.filter(name__icontains=search_query)

    # Pass filtered leads and filter states to the template
    context = {
        'leads': leads,
        'selected_status': status,
        'selected_source': source,
        'selected_medium': medium,
        'search_query': search_query
    }
    return render(request, 'api/lead_dashboard.html', context)


# Create Lead View (Handles Form Data Submission)
@csrf_exempt  # Only for local testing
def create_lead(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse incoming JSON data

            # Debugging log (Prints the data received from JavaScript)
            print("Data received: ", data)

            # Check if data contains required fields
            if 'name' not in data or 'email' not in data or not data['name'] or not data['email']:
                return JsonResponse({'error': 'Name and email are required fields.'}, status=400)

            # Save data to the database
            Lead.objects.create(
                name=data.get('name', ''),
                email=data.get('email', ''),
                phone = data.get('phone',''),
                message= data.get('message', ''),
                status='Unique Lead',
                source='JavaScript Tracker',
                medium='Web Form'
            )

            return JsonResponse({'message': 'Lead captured successfully.'}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@method_decorator(csrf_exempt, name='dispatch')  # Only for local testing
class LeadCreateView(APIView):

    def post(self, request):
        serializer = LeadSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Lead captured successfully."}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
