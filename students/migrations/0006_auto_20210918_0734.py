# Generated by Django 2.2.20 on 2021-09-18 07:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20210918_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendon',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, primary_key=True, serialize=False),
        ),
    ]