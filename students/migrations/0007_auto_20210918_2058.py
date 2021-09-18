# Generated by Django 2.2.20 on 2021-09-18 15:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20210918_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendon',
            name='id',
            field=models.AutoField(auto_created=True, default=django.utils.timezone.now, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendon',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
