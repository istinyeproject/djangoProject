from django.db import models
from django.utils import timezone


class Publication(models.Model):
    authors = models.JSONField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    link = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Publications"


class Person:
    image = models.ImageField()
    name = models.CharField()
    title = models.CharField()
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "People"