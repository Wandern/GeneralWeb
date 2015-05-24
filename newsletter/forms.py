from django import forms

from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Examples of additional types of validators.
        # email_base, provider = email.split('@')
        # domain, extension = provider.split('.')
        # if domain != 'UB':
        #     raise forms.ValidationError("Please make sure you use you UB email address.")
        # if extension != 'edu':
        #     raise forms.ValidationError("Please make sure to use a valid EDU email address.")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name
