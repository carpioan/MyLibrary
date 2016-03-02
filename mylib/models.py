from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

# Create your models here.

class PublishingPress(models.Model):
    publishing_press = models.CharField(max_length=30)

    def __str__(self):
        return self.publishing_press

class Author(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name

class Book(models.Model):
    authors = models.ManyToManyField(Author, blank=False, default=None)
    book_title = models.CharField(max_length=200)
    book_edition = models.IntegerField(default=1)
    book_theme = models.CharField(max_length=30, blank=False)
    publishing_year = models.IntegerField(blank=False)
    publishing_presses = models.ManyToManyField(PublishingPress, blank=False, default=None)
    registered_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.book_title


        class Meta():
            ordering = ('registered_date')
