# Generated by Django 5.1.3 on 2024-11-06 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.TextField(default='Default Address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='booking_phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='booking_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='contact_phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='contact_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='county',
            field=models.CharField(default='Default County', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(default='Default Event', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='is_free_to_visit',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='venue_name',
            field=models.CharField(default='Default Venue', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
