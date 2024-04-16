from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"

        widgets = {

            "passenger_name": forms.TextInput(attrs={"class": "form-control"}),
            "passenger_email": forms.EmailInput(attrs={"class": "form-control"}),
            "booking_date": forms.DateInput(attrs={"type": "date"}),
            "where_to_go": forms.TextInput(attrs={"class": "form-control"}),
            "number_of_tickets": forms.TextInput(attrs={"class": "form-control"}),

        }