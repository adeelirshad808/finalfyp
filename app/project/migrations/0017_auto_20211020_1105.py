# Generated by Django 3.2.8 on 2021-10-20 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_auto_20211020_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='assignment_status',
        ),
        migrations.RemoveField(
            model_name='submissions',
            name='sub_status',
        ),
        migrations.AddField(
            model_name='submissions',
            name='submission_title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.assignment'),
        ),
    ]
