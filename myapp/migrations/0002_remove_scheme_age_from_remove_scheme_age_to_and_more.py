# Generated by Django 4.2.13 on 2024-06-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheme',
            name='age_from',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='age_to',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='json_data',
        ),
        migrations.AddField(
            model_name='scheme',
            name='lower_age',
            field=models.IntegerField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='scheme',
            name='upper_age',
            field=models.IntegerField(blank=True, max_length=255, null=True),
        ),
    ]
