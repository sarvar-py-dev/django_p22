# Generated by Django 5.0.6 on 2024-06-17 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_cards'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cards',
            old_name='name',
            new_name='full_name',
        ),
    ]