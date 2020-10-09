from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.BigAutoField(
        primary_key=True,
    )

    name = models.CharField(
        verbose_name='Category Name',
        max_length=15,
        unique=True,
        blank=False,
        null=False,
    )

    description = models.TextField(
        verbose_name='Description',
        max_length=5000,
        blank=False,
        null=False
    )

    slug = models.SlugField(
        max_length=20,
        blank=False,
        null=False
    )