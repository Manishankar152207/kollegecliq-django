# Generated by Django 4.1.1 on 2022-09-23 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_registeredusers_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredusers',
            name='name',
            field=models.CharField(max_length=55, null=True),
        ),
    ]
