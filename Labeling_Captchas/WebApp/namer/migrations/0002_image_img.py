# Generated by Django 2.0.1 on 2018-01-25 18:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('namer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media'),
            preserve_default=False,
        ),
    ]