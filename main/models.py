from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    isbn = models.CharField(max_length=15, primary_key=True)
    book_name = models.CharField(max_length=50, blank=True)
    author = models.CharField(max_length=30)
    image = models.ImageField(upload_to='imgs')
    publish_date = models.DateField(auto_created=True)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    publisher = models.ForeignKey(User, on_delete=models.RESTRICT)
