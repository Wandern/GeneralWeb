from django.contrib import admin

# Register your models here.
from .forms import ContactForm
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ["full_name", "__unicode__", "created_on", "updated_on"]
    form = ContactForm


admin.site.register(Contact, ContactAdmin)
