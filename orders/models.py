from django.db import models
from robots.models import Robot

class Order(models.Model):
    order_number = models.CharField(max_length=10, blank=False, null=False)
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number