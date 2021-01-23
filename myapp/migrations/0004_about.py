# Generated by Django 3.1 on 2020-09-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_award'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]
