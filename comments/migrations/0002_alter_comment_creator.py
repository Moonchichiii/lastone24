# Generated by Django 5.0.1 on 2024-03-01 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('profiles', '0002_remove_profile_content_remove_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_created', to='profiles.profile'),
        ),
    ]
