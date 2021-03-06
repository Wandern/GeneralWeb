from django.db import models


# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=False, null=True)
    message = models.CharField(max_length=300, blank=False, null=True)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):  # Python 3.3 is __str__
        return self.email

# Create your models here.
