# Generated by Django 4.0.4 on 2022-05-17 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_owned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='atk',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='card',
            name='attribute',
            field=models.CharField(default='N/A', max_length=20),
        ),
        migrations.AlterField(
            model_name='card',
            name='defense',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='card',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='card',
            name='property',
            field=models.CharField(default='N/A', max_length=20),
        ),
        migrations.AlterField(
            model_name='card',
            name='type',
            field=models.CharField(default='N/A', max_length=100),
        ),
    ]
