# Generated by Django 5.1.2 on 2024-11-19 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0039_alter_basicinfo_swsj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinfo',
            name='ztrybh',
            field=models.CharField(db_index=True, max_length=50, verbose_name='在逃人员编号'),
        ),
    ]
