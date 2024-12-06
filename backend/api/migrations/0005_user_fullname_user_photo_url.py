# Generated by Django 5.1.3 on 2024-11-29 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_chat_bot_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='photo_url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
