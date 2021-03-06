# Generated by Django 3.0.4 on 2020-03-22 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=250)),
                ('ticket_type', models.CharField(choices=[('free', 'FREE'), ('paid', 'PAID')], default='free', max_length=10)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.IntegerField(choices=[(0, 'disabled'), (1, 'active')], default=1)),
                ('image', models.ImageField(blank=True, upload_to='event_image')),
                ('slug', models.SlugField(default='', editable=False, max_length=255)),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.EventType')),
                ('organiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
