# Generated by Django 3.1.1 on 2020-10-20 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20201020_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='code_refund',
            field=models.CharField(default='test_code', max_length=50),
            preserve_default=False,
        ),
    ]