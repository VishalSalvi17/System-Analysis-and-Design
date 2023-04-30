# Generated by Django 3.1.1 on 2020-09-15 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('day', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
        ),
    ]
