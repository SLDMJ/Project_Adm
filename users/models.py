
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserMsg(models.Model):

    name = models.CharField(max_length=20, verbose_name="")
    hwnum = models.CharField(max_length=20, verbose_name="")
    psw = models.CharField(max_length=20, verbose_name="")
    hwdev = models.CharField(max_length=20, verbose_name="")
    fnstdev = models.CharField(max_length=20, verbose_name="")


