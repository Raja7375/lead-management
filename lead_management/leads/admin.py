from django.contrib import admin
from .models import Category, LeadSource, Lead, LeadFeedback

admin.site.register(Category)
admin.site.register(LeadSource)
admin.site.register(Lead)
admin.site.register(LeadFeedback)
