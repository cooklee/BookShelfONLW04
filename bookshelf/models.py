from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Publisher(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)

class Book(models.Model):
    title = models.CharField(max_length=64)
    year = models.IntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
