# Generated by Django 5.1.1 on 2024-09-16 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_record_sana'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='sana',
        ),
    ]
