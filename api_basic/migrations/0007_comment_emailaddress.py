# Generated by Django 3.1.14 on 2022-05-26 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0006_auto_20220522_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='emailAddress',
            field=models.EmailField(max_length=255, null=True),
        ),
    ]
