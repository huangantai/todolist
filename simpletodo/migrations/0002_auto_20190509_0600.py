# Generated by Django 2.1.7 on 2019-05-09 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpletodo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
