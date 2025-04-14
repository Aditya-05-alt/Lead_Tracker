from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    # Tracking fields
    page_link = models.URLField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)  # changed from URLField
    medium = models.CharField(max_length=100, blank=True, null=True)
    dealer = models.CharField(max_length=100, blank=True, null=True)

    # UTM tracking
    utm_campaign = models.CharField(max_length=255, blank=True, null=True)
    utm_term = models.CharField(max_length=255, blank=True, null=True)
    utm_content = models.CharField(max_length=255, blank=True, null=True)

    # Lead status
    status = models.CharField(
        max_length=50,
        choices=[('Unique Lead', 'Unique Lead'), ('Repeat Lead', 'Repeat Lead')],
        default='Unique Lead',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email or self.phone or "Lead"
