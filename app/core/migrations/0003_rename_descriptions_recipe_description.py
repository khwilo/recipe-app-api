# Generated by Django 3.2.25 on 2024-07-27 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='descriptions',
            new_name='description',
        ),
    ]
