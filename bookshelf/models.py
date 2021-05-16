from django.db import models


# Create your models here.
from django.urls import reverse


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

    def __str__(self):
        return f"{self.title} {self.year}"


    def get_absolute_url(self):
        return reverse("update_book", args=(self.pk,))


class BookReview(models.Model):
    date = models.DateField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    rate = models.IntegerField()

    def __str__(self):
        return f"{self.date} {self.book.title} {self.text} {self.rate}"


