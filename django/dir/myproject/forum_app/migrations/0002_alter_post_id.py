# Generated by Django 5.1.5 on 2025-01-22 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
