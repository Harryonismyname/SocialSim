# Generated by Django 2.2 on 2020-11-05 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='last_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
