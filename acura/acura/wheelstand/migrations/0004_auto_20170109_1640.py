# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheelstand', '0003_auto_20170107_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exteriorcolour',
            name='md5',
            field=models.CharField(default=b'22036b5f65483a5b9d5a53a97196a0ce', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='md5',
            field=models.CharField(default=b'efa3b75c7b2c2ad416b40fe61053dadd', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='interiors',
            name='md5',
            field=models.CharField(default=b'b85c74ef5329506647d0ad9fb6c4a0e4', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='models',
            name='md5',
            field=models.CharField(default=b'2c6323fc2fb006e88e5836a421ec6656', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='modelsshown',
            name='md5',
            field=models.CharField(default=b'6bd21d7ba74dc0462b5185464608a0d4', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='trim',
            name='md5',
            field=models.CharField(default=b'5c76d0a934c3f4f1f8325077c32acf54', max_length=255, editable=False),
        ),
    ]
