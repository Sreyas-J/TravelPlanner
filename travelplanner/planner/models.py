from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_name=models.CharField(max_length=50,null=True)
    from_loc=models.CharField(max_length=100,null=True)
    to=models.CharField(max_length=100,null=True)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.FloatField()

    def __str__(self):
        return f'{self.flight_name}:from {self.from_loc} to {self.to} at {self.departure_time} - {self.arrival_time} for Rs.{self.price}'