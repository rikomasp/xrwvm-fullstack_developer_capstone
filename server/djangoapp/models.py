"""Models for the Cars Dealership app."""
from django.db import models


class CarMake(models.Model):
    """Represents a car manufacturer."""
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    """Represents a car model."""
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dealer_id = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.car_make.name} {self.name}"


class Dealer(models.Model):
    """Represents a car dealership."""
    full_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


class Review(models.Model):
    """Represents a dealer review."""
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length=100)
    review_text = models.TextField()
    sentiment = models.CharField(max_length=20, default='neutral')
    purchase_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer} - {self.dealer.short_name}"
