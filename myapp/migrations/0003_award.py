# Generated by Django 3.1 on 2020-09-08 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=100)),
            ],
        ),
    ]
