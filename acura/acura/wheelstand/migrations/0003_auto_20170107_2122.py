# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wheelstand', '0002_auto_20170102_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='exteriorcolour',
            name='name',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='modelsshown',
            name='disclaimer_en',
            field=models.TextField(help_text='English', max_length=500, null=True, verbose_name=b'Disclaimer English', blank=True),
        ),
        migrations.AddField(
            model_name='modelsshown',
            name='disclaimer_fr',
            field=models.TextField(help_text='French', max_length=500, null=True, verbose_name=b'Disclaimer French', blank=True),
        ),
        migrations.AddField(
            model_name='modelsshown',
            name='link',
            field=models.CharField(max_length=255, null=True, verbose_name='OR Remote URL', blank=True),
        ),
        migrations.AddField(
            model_name='modelsshown',
            name='md5',
            field=models.CharField(default=b'e8de784393542ecb2df34ebb1498a5d3', max_length=255, editable=False),
        ),
        migrations.AddField(
            model_name='modelsshown',
            name='status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, editable=False, monitor=b'url'),
        ),
        migrations.AddField(
            model_name='modelsshown',
            name='url',
            field=models.ImageField(upload_to=b'uploads/modelsshown/', null=True, verbose_name='Image', blank=True),
        ),
        migrations.AlterField(
            model_name='exteriorcolour',
            name='md5',
            field=models.CharField(default=b'c0deb7c32b87df0f889ea6d5f10a068b', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='md5',
            field=models.CharField(default=b'971ea2c9e1176901c386d9067907dfad', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='interiors',
            name='md5',
            field=models.CharField(default=b'6981607251ed2f930083124f37e948d2', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='models',
            name='md5',
            field=models.CharField(default=b'075302fc92fef260bf8d7baf3ebfc284', max_length=255, editable=False),
        ),
        migrations.RemoveField(
            model_name='modelsshown',
            name='accessory',
        ),
        migrations.AddField(
            model_name='modelsshown',
            name='accessory',
            field=models.ManyToManyField(to='wheelstand.Accessories', blank=True),
        ),
        migrations.AlterField(
            model_name='trim',
            name='md5',
            field=models.CharField(default=b'f7787f206ddb315b3544ba29f09c9875', max_length=255, editable=False),
        ),
    ]
