# Generated by Django 4.0.6 on 2022-09-17 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.CharField(max_length=55, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=55)),
                ('phone', models.CharField(max_length=14)),
                ('password', models.CharField(max_length=260)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField()),
                ('is_live', models.CharField(max_length=2)),
            ],
        ),
    ]
