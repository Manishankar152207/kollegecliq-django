# Generated by Django 4.1.1 on 2022-10-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_registeredcollege_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredcollege',
            name='user_id',
            field=models.CharField(default='34953b0e-012c-43db-b6ed-e3eb6ffee968', max_length=55, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='registeredusers',
            name='user_id',
            field=models.CharField(default='6d308461-d949-42be-af2e-94fc62983ee1', max_length=55, primary_key=True, serialize=False),
        ),
    ]
