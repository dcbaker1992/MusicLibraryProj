# Generated by Django 3.1.8 on 2021-06-11 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
