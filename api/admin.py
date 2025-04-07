from django.contrib import admin

from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject','message', 'status', 'pagelink','source', 'medium', 'created_at')
    list_filter = ('status', 'source', 'medium')
    search_fields = ('name', 'email', 'phone')
