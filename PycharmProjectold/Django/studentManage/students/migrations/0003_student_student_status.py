# Generated by Django 3.1 on 2020-08-23 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20200823_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_status',
            field=models.IntegerField(choices=[('0', 'di hoc'), ('1', 'di lam')], default=1, max_length=1),
        ),
    ]
