# Generated by Django 2.1.5 on 2020-03-07 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mammoth', '0014_pattern_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='pattern',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]