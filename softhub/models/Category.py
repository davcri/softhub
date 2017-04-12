from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
