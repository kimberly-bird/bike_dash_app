from django.contrib.auth.models import User
from django.db import models


class Bike_User(models.Model):
    last_signon = models.CharField(blank=True, max_length=15, default='2019-01-01')
    street = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip = models.PositiveSmallIntegerField(blank=True)
    phone = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"