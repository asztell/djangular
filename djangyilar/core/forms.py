from django import forms
from core.models import Email
# from django.utils import timezone


class ContactForm(forms.ModelForm):
    # contact_name = forms.CharField(required=True)
    # contact_email = forms.EmailField(required=True)
    # # content = forms.CharField(
    #     required=True,
    #     widget=forms.Textarea
    # )

    # created_date = forms.DateTimeField(required=True)


    class Meta:
        model = Email
        # fields = "__all__"
        fields = [
        'contact_name',
        'contact_email',
        'content',
    ]
