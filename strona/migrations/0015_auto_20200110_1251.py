# Generated by Django 3.0.2 on 2020-01-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0014_addingstats_deletingstats_deliveringstats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addingstats',
            name='counter',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='deletingstats',
            name='counter',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='deliveringstats',
            name='counter',
            field=models.SmallIntegerField(default=0),
        ),
    ]