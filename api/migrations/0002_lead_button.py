# Generated by Django 5.1.7 on 2025-03-20 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='button',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
