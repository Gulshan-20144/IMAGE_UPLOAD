# Generated by Django 5.0.2 on 2024-03-14 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserImage', '0002_rename_date_of_birth_user_dob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='image',
            new_name='image_field',
        ),
    ]
