# Generated by Django 3.0.2 on 2020-02-07 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200206_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='dest_lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='dest_lng',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
