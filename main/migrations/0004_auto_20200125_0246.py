# Generated by Django 3.0.2 on 2020-01-25 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200125_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoir',
            name='training_given_specify',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
