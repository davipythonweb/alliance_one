from django.db import models

class Cars(models.Model):
    name = models.CharField(max_length=10)
    brand = models.CharField(max_length=10)
    release_date = models.DateField(null=True, blank=False)

    class Meta:
        ordering = ['name', 'brand']

    def __str__(self):
        return f'{self.name}, {self.brand},{self.release_date}'
    