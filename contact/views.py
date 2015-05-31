from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.


def contact(request):
    title_align_center = True
    form = ContactForm(request.POST or None)
    context = {
        "submit_value": "Submit",
        "title": "Contact Us",
        "form": form,
        "title_align_center": title_align_center,
    }
    if request.method == 'POST':
        if form.is_valid():
            form_email = form.cleaned_data.get("email")
            form_message = form.cleaned_data.get("message")
            form_full_name = form.cleaned_data.get("full_name")
            subject = "Site Contact Form"
            from_email = settings.EMAIL_HOST_USER
            to_email = ["daniel@terrakarma.us"]
            contact_message = " %s: %s via %s" % (form_full_name, form_message, form_email)

            send_mail(subject, contact_message, from_email, to_email, fail_silently=False)

            form.save()
            context = {
                "title": "Thank You"
            }
            return HttpResponseRedirect('/', context)
    else:
        return render(request, "forms.html", context)


def thanks(request):
    context = request.context
    return render(request, "thanks.html", context)
