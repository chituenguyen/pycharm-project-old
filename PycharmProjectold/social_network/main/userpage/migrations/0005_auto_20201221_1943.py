# Generated by Django 3.1.4 on 2020-12-21 12:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userpage', '0004_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='likingUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
