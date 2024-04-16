from django.db import models


class Ticket(models.Model):
    passenger_name = models.CharField(max_length=30)
    passenger_email = models.EmailField()
    booking_date = models.DateField()
    where_to_go = models.CharField(max_length=20)
    number_of_tickets = models.IntegerField()
