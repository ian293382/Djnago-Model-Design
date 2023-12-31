# Generated by Django 5.0 on 2023-12-06 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_comment_todolist'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='comments',
            field=models.ManyToManyField(to='client.comment'),
        ),
        migrations.AddField(
            model_name='todolist',
            name='comments',
            field=models.ManyToManyField(to='client.comment'),
        ),
    ]
