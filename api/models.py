from django.db import models
# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
   
    subject = models.TextField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, choices=[
        ('Unique Lead', 'Unique Lead'),
        ('Repeat Lead', 'Repeat Lead'),
    ])
    page_link = models.URLField(null=True, blank=True)
    source = models.URLField(null=True, blank=True)
    medium = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # button = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.email or self.phone or "Lead"