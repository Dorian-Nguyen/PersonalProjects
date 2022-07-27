from django.db import models
import csv
from django.conf import settings


class StatementUpload(models.Model):
    csv_file = models.FileField(upload_to='uploads/')

class Transaction(models.Model):
    date = models.CharField('date',max_length=100)
    amount = models.FloatField("amount")
    desc = models.CharField("desc", max_length=100)
    category = models.CharField("desc", max_length=100)
    bank = models.CharField("bank", max_length=100)
