# Generated by Django 3.1.14 on 2022-05-26 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0011_auto_20220526_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='emailAddress',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
