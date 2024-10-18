from django.contrib import admin
from .models import NewsletterSignup  

class NewsletterSignupAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscribed_at') 
    search_fields = ('name', 'email') 

admin.site.register(NewsletterSignup, NewsletterSignupAdmin)
