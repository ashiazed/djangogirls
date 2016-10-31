# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-31 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0019_auto_20160628_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='rsvp_no_code',
            field=models.CharField(default='', max_length=24),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='rsvp_yes_code',
            field=models.CharField(default='', max_length=24),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='state',
            field=models.CharField(choices=[(b'submitted', b'Application submitted'), (b'accepted', b'Application accepted'), (b'rejected', b'Application rejected'), (b'waitlisted', b'Application on waiting list'), (b'declined', b'Applicant declined')], default=b'submitted', max_length=50, verbose_name=b'State of the application'),
        ),
        migrations.AlterField(
            model_name='email',
            name='failed_to_sent',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='email',
            name='successfuly_sent',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='score',
            name='comment',
            field=models.TextField(blank=True, default='', help_text=b'Any extra comments?'),
            preserve_default=False,
        ),
    ]