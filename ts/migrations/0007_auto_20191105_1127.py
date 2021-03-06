# Generated by Django 2.2 on 2019-11-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ts', '0006_auto_20190604_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phase',
            name='light_mode',
        ),
        migrations.RemoveField(
            model_name='thermostat',
            name='light_mode',
        ),
        migrations.AddField(
            model_name='phase',
            name='light_UV',
            field=models.IntegerField(default=0, verbose_name='UV'),
        ),
        migrations.AddField(
            model_name='thermostat',
            name='light_UV',
            field=models.IntegerField(default=0, verbose_name='UV'),
        ),
        migrations.AlterField(
            model_name='phase',
            name='light',
            field=models.IntegerField(default=0, verbose_name='Стан освітлення'),
        ),
        migrations.AlterField(
            model_name='thermostat',
            name='light',
            field=models.IntegerField(default=0, verbose_name='Стан освітлення'),
        ),
    ]
