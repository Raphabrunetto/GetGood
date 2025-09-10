from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} em {self.date}"
