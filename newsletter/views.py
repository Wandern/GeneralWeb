from django.shortcuts import render

from .forms import SignUpForm



# Create your views here.
def home(request):
    submit_value = "SignUp"
    title = "Newsletter Signup"
    greeting = title + " SignUp"


    form = SignUpForm(request.POST or None)

    context = {
        "submit_value": submit_value,
        "title": title,
        "greeting": greeting,
        "form": form
    }

    if form.is_valid():
        form.save()
        context = {
            "title": "Thank You"
        }

    return render(request, "index.html", context)
