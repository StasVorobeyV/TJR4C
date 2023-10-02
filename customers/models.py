from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    # address = models.CharField(max_length=200, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
