# Generated by Django 3.2.12 on 2022-02-09 06:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_channels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('video_file', models.FileField(upload_to='')),
                ('thumbnail', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('licence', models.CharField(choices=[('U', 'Universal'), ('S', 'Universal/Adult'), ('A', 'Adult'), ('X', 'XXX-Content')], max_length=1)),
                ('date_uploaded', models.DateField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('good', models.BigIntegerField(default=0)),
                ('bad', models.BigIntegerField(default=0)),
                ('views', models.BigIntegerField(default=0)),
                ('playlist', models.ForeignKey(blank=True, default='playlists', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='videos', to='user_channels.playlist')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
    ]