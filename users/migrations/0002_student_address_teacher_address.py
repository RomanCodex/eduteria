# Generated by Django 4.2.2 on 2023-06-23 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(default='a', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='address',
            field=models.CharField(default='a', max_length=256),
            preserve_default=False,
        ),
    ]
