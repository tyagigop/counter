from django.db import models


class DateNumberEntry(models.Model):
    date = models.DateField(unique=True)
    number = models.IntegerField(default=0)

    def __str__(self):
        return f"Date: {self.date}, Number: {self.number}"

