# Generated by Django 3.2.9 on 2021-11-09 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0001_initial'),
        ('chatmessages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='uploaded_audio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='uploads.uploadedaudio'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='uploaded_file',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='uploads.uploadedfile'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='uploaded_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='uploads.uploadedimage'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='uploaded_video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='uploads.uploadedvideo'),
        ),
    ]