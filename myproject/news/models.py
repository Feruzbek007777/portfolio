# models.py
from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    about = models.TextField(null=True, blank=True, verbose_name="O'zingiz haqingizda: ")
    image = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="Rasmi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Portfolio"


class Experience(models.Model):
    name_language = models.CharField(max_length=100, verbose_name="Dasturlash tili")
    experience = models.CharField(max_length=150, verbose_name="Tajribangiz")

    def __str__(self):
        return self.name_language


class Awards(models.Model):
    name = models.CharField(max_length=100, verbose_name="Mukofot nomi: ")
    experience = models.CharField(max_length=150, verbose_name="Tajribangiz: ")

    def __str__(self):
        return self.name


class Skills(models.Model):
    title = models.CharField(max_length=250, verbose_name="Skillar")

    def __str__(self):
        return self.title
