# Generated by Django 3.1.2 on 2020-11-29 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='flag',
            field=models.BooleanField(default=False),
        ),
    ]
