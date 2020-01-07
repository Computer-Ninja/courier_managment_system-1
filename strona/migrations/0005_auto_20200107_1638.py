# Generated by Django 3.0 on 2020-01-07 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0004_auto_20191210_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='oldchange',
            name='package_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='strona.PackageType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='packagechange',
            name='package_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='strona.PackageType'),
            preserve_default=False,
        ),
    ]
