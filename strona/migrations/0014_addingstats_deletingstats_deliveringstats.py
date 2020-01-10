# Generated by Django 3.0.2 on 2020-01-10 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0013_auto_20200110_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddingStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('counter', models.SmallIntegerField()),
            ],
            options={
                'ordering': ['-date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeletingStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('counter', models.SmallIntegerField()),
            ],
            options={
                'ordering': ['-date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeliveringStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('counter', models.SmallIntegerField()),
            ],
            options={
                'ordering': ['-date'],
                'abstract': False,
            },
        ),
    ]
