from django.db import models


class City(models.Model):
    name = models.CharField(verbose_name="Город", max_length=64)

    def __srt__(self):
        return self.name
