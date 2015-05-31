from django.shortcuts import render
from .models import About

# Create your views here.
def about(request):

    abt = About.objects.get(active=True)
    title = abt.title
    message = abt.message

    # if request.user.is_authenticated():
    #     greeting = "Hello %s" % request.user

    context = {
        "title": title,
        "message": message
    }

    return render(request, "about.html", context)

