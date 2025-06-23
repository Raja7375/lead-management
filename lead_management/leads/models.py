from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

class LeadSource(models.Model):
    name = models.CharField(max_length=255)

class Lead(models.Model):
    date = models.DateField(auto_now_add=True)
    agent = models.ForeignKey(User, related_name='leads_added', on_delete=models.CASCADE)
    client_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    matter = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    lead_source = models.ForeignKey(LeadSource, on_delete=models.SET_NULL, null=True)
    assigned_lawyer = models.ForeignKey(User, related_name='leads_received', on_delete=models.SET_NULL, null=True)

class LeadFeedback(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
