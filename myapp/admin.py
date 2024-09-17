# admin.py
from django.contrib import admin
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'hodim_fish','sana', 'viloyat', 'tuman', 'aloqa_bolimi_nomi')
