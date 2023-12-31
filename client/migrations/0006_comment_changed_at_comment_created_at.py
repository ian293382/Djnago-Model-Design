# Generated by Django 5.0 on 2023-12-06 17:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_alter_client_options_remove_comment_changed_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='changed_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
