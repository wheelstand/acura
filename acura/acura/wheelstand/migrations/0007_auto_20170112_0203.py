# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheelstand', '0006_auto_20170110_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='engines',
            name='activeControl',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='engines',
            name='hyBridPowerTrain',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='engines',
            name='hybridHorsePower',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='engines',
            name='hybridTorque',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='engines',
            name='idelStop',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='engines',
            name='vcm',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='exteriorcolour',
            name='md5',
            field=models.CharField(default=b'dc922e9cc6b9f211b8aa5cb1bbc91b12', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ForeignKey(related_name='gallery', blank=True, to='wheelstand.Models', null=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='md5',
            field=models.CharField(default=b'f30c1f697d1eb7ffc14808aa555ebdb3', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='interiors',
            name='md5',
            field=models.CharField(default=b'3f7888771b9fdf5b95b82e4ccee2856b', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='models',
            name='md5',
            field=models.CharField(default=b'1711589f687d6614ea0ecb691f4ea61c', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='modelsshown',
            name='md5',
            field=models.CharField(default=b'e9ff7b272c1bd1494bc7e7a58c4a4ec4', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='trim',
            name='md5',
            field=models.CharField(default=b'2e7076063edbad967c844f6bbdf97e5c', max_length=255, editable=False),
        ),
    ]
