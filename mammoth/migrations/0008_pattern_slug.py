# Generated by Django 2.1.5 on 2020-02-25 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mammoth', '0007_pattern'),
    ]

    operations = [
        migrations.AddField(
            model_name='pattern',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
