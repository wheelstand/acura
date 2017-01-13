# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheelstand', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exteriorcolour',
            name='md5',
            field=models.CharField(default=b'c02460237967242c0b075c925e196970', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='md5',
            field=models.CharField(default=b'ea481d3617737ac8576fb8867ad85011', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='interiors',
            name='md5',
            field=models.CharField(default=b'772af274035bfedcce16fcbc7bcdf9c5', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='models',
            name='md5',
            field=models.CharField(default=b'b9f8caa4037da8f0eabee066578ecc87', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='trim',
            name='md5',
            field=models.CharField(default=b'bb9021d58fa8367136d06a309b2a63e9', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='trim',
            name='model',
            field=models.ForeignKey(related_name='trims', blank=True, to='wheelstand.Models', null=True),
        ),
        migrations.RemoveField(
            model_name='trim',
            name='transmission',
        ),
        migrations.AddField(
            model_name='trim',
            name='transmission',
            field=models.ManyToManyField(to='wheelstand.Transmissions', blank=True),
        ),
    ]
