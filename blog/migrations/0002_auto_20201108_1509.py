# Generated by Django 3.1.3 on 2020-11-08 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
