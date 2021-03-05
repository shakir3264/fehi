from django.db import models


class Companies(models.Model):
    company = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.company}"



class Guest(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    passport = models.CharField(max_length=40)
    nationality = models.CharField(max_length=40)
    phone = models.DecimalField(max_digits=15, decimal_places=0)
    category = models.CharField(max_length=40)
    company = models.ForeignKey('Companies', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.email} {self.passport} {self.nationality}"


