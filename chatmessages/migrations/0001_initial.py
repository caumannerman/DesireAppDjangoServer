# Generated by Django 3.2.9 on 2021-11-08 12:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='작성 시각')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='수정 시각')),
            ],
        ),
    ]
