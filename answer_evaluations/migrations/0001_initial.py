# Generated by Django 3.2.9 on 2021-11-08 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerEvaluation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('evaluation', models.CharField(choices=[('NG', 'Not good enough'), ('OK', 'Okay'), ('GR', 'Great')], default='OK', max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='작성 시각')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='수정 시각')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='answers.answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]