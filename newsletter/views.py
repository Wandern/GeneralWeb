from django.shortcuts import render

from .forms import SignUpForm


# Create your views here.
def newsletter(request):
    title = "Hello New User"
    if request.user.is_authenticated():
        title = "Hello %s" % request.user

    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        form.save()
        context = {
            "title": "Thank You"
        }

    return render(request, "forms.html", context)
