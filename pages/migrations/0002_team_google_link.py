# Generated by Django 3.2 on 2023-04-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='google_link',
            field=models.URLField(max_length=100, null=True),
        ),
    ]