# Generated by Django 5.1.2 on 2024-10-29 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0020_remove_basicinfo_gxr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicinfo',
            name='dtbd',
        ),
        migrations.RemoveField(
            model_name='basicinfo',
            name='jtbd',
        ),
        migrations.RemoveField(
            model_name='basicinfo',
            name='yp',
        ),
    ]
