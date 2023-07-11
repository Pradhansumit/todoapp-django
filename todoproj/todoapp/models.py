from django.db import models

# Create your models here.


class TodoModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField()
    address = models.CharField(max_length=500)

    class Meta:
        ordering = ["id"]
