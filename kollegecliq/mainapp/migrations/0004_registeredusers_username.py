# Generated by Django 4.1.1 on 2022-09-22 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_registeredusers_delete_registerusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredusers',
            name='username',
            field=models.CharField(default=0, max_length=55),
        ),
    ]
