# Generated by Django 4.2.2 on 2024-10-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.CharField(default='', max_length=100),
        ),
    ]