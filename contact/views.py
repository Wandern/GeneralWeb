from django.shortcuts import render

from .forms import ContactForm
# Create your views here.


def contact(request):
    form = ContactForm(request.POST or None)

    context = {
        "title": "Contact Us",
        "form": form
    }

    if form.is_valid():
        form.save()
        context = {
            "title": "Thank You"
        }
    return render(request, "forms.html", context)
