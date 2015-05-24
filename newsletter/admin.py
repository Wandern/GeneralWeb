from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import SignUp


class SignUpAdmin(admin.ModelAdmin):
    list_display = ["full_name", "__unicode__", "created_on", "updated_on"]
    form = SignUpForm
    # class Meta:
    #     model = SignUp

admin.site.register(SignUp, SignUpAdmin)
