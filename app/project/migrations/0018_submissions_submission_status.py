# Generated by Django 3.2.8 on 2021-10-20 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_auto_20211020_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissions',
            name='submission_status',
            field=models.BooleanField(default=False),
        ),
    ]