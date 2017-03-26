from django.db import models


class License(models.Model):
    license = models.CharField(max_length=100, unique=True)

    choices = (
        ('gpl', 'GPL'),
        ('gplv2', 'GPL v2'),
        ('gplv3', 'GPL v3'),
        ('mit', 'MIT'),
        ('apache', 'Apache'),
        ('closed source', 'Closed Source')
    )
    license.choices = choices

    def __str__(self):
        return self.license
