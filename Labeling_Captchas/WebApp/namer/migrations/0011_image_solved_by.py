# Generated by Django 2.0.1 on 2018-01-27 04:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('namer', '0010_auto_20180126_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='solved_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
