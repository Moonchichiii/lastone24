# Generated by Django 5.0.1 on 2024-03-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_remove_profile_content_remove_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../Defaultprofile_tvf0tm.png', upload_to='images/'),
        ),
    ]
