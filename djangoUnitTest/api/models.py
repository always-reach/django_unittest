from django.db import models


# Create your models here.

class SampleTable(models.Model):
    name = models.CharField(verbose_name="氏名", max_length=10)
    phone = models.IntegerField(verbose_name="電話番号")
