# Generated by Django 5.1.2 on 2024-11-22 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0051_alter_ypbg_swsj'),
    ]

    operations = [
        migrations.AddField(
            model_name='backout',
            name='fz',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='分值'),
        ),
    ]
