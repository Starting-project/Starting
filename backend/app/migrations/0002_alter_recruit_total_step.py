# Generated by Django 4.1 on 2022-08-11 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruit',
            name='total_step',
            field=models.IntegerField(),
        ),
    ]
