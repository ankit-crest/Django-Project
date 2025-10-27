from django.db import models

# Create your models here.

class Members(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)

    class Meta:
        db_table = 'members'
    def __str__(self):
        return self.name