# Generated by Django 4.2.11 on 2024-04-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pic')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=50)),
            ],
        ),
    ]
