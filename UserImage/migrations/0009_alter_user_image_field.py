# Generated by Django 5.0.2 on 2024-03-14 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserImage', '0008_alter_user_image_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image_field',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
