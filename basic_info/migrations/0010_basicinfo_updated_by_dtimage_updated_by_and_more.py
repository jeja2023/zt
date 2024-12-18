# Generated by Django 5.1.2 on 2024-10-22 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0009_alter_gxr_gxr_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicinfo',
            name='updated_by',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='更新人'),
        ),
        migrations.AddField(
            model_name='dtimage',
            name='updated_by',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='更新人'),
        ),
        migrations.AddField(
            model_name='gxr',
            name='updated_by',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='更新人'),
        ),
        migrations.AddField(
            model_name='gz',
            name='updated_by',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='更新人'),
        ),
        migrations.AddField(
            model_name='jtimage',
            name='updated_by',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='更新人'),
        ),
        migrations.AddField(
            model_name='sfyj',
            name='updated_by',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='更新人'),
        ),
        migrations.AddField(
            model_name='swimage',
            name='updated_by',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='更新人'),
        ),
        migrations.AddField(
            model_name='ypbg',
            name='updated_by',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='更新人'),
        ),
        migrations.AddField(
            model_name='ypjl',
            name='updated_by',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='更新人'),
        ),
        migrations.AddField(
            model_name='zhzg',
            name='updated_by',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='更新人'),
        ),
    ]
