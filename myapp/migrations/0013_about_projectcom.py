# Generated by Django 3.1 on 2020-09-26 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20200926_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='projectcom',
            field=models.IntegerField(default=True),
            preserve_default=False,
        ),
    ]
