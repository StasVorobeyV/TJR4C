from django.db import models

class Robot(models.Model):
    serial = models.CharField(max_length=2, choices=[
        ('D1', 'D1'),
        ('D2', 'D2'),
        ('D3', 'D3'),
        ('D4', 'D4')
    ], blank=False, null=False)
    model = models.CharField(max_length=2, choices=[
        ('R1', 'R1'),
        ('R2', 'R2'),
        ('R3', 'R3'),
        ('R4', 'R4')
    ], blank=False, null=False)
    name = models.CharField(max_length=10, default='', choices=[
        ('light', 'Light'),
        ('edition', 'Edition'),
        ('pro', 'Pro')
    ])
    created = models.DateTimeField(auto_now_add=True)

    @property
    def formatted_model(self):
        return f"R{self.model}"

    @property
    def formatted_version(self):
        return f"D{self.serial}"