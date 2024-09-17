# models.py
from django.db import models
from django.utils import timezone

class Record(models.Model):
    barcode = models.CharField(max_length=255)
    hodim_fish = models.CharField(max_length=255)
    viloyat = models.CharField(max_length=255)
    tuman = models.CharField(max_length=255)
    aloqa_bolimi_nomi = models.CharField(max_length=255)
    rasm = models.ImageField(upload_to='images/',null=True, blank=True)
    sana = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return self.barcode
