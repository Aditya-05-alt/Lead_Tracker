from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializer import LeadSerializer
from .models import Lead
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from rest_framework import status
import json


# Render your HTML form
def index(request):
    return render(request, 'api/index.html')


# Admin-style dashboard view
def lead_dashboard(request):
    leads = Lead.objects.all().order_by('-created_at')

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


# ✅ Lead capture view for JS tracker
@method_decorator(csrf_exempt, name='dispatch')
class LeadCreateView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            # Manually decode if content is JSON
            if request.content_type == "application/json":
                data = json.loads(request.body.decode('utf-8'))
            else:
                data = request.data

            print("📩 Incoming lead data:", data)

            name = data.get('name') or data.get('id_name') or data.get('class_name')
            email = data.get('email') or data.get('id_email') or data.get('class_email')
            phone = data.get('phone', '') or data.get('id_phone') or data.get('class_phone') or data.get("your-phone")
            message = data.get('message', '') or data.get('your-message') or data.get('id_message')
            subject = data.get('subject', '')

            # These now come from JS
            pagelink = data.get('page_link', 'JS Tracker Unknown Site')
            source = data.get('source',"Direct")

            medium = data.get('medium', 'Web Form')

            # if not name or not email:
            #     return Response({'error': 'Name and Email are required.'}, status=status.HTTP_400_BAD_REQUEST)

            lead = Lead.objects.create(
                name=name,
                email=email,
                phone=data.get('phone', ''),
                subject=data.get('subject', ''),
                message= message,
                page_link=data.get('page_link', ''),
                source=data.get('source', ''),
                medium=data.get('medium', 'Web Form'),
                status='Unique Lead'
            )

            return Response({"message": "Lead captured successfully ✅"}, status=status.HTTP_201_CREATED)

        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
