# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheelstand', '0004_auto_20170109_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exteriorcolour',
            name='md5',
            field=models.CharField(default=b'a8bd8d50ee495345f02b7ea350e61ac4', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='md5',
            field=models.CharField(default=b'fac21dd373681c5840523b921671d4ab', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='interiors',
            name='md5',
            field=models.CharField(default=b'1570dd2c1c6808b4ccf478235a9f6bef', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='models',
            name='md5',
            field=models.CharField(default=b'0c9f9cd11f42f6649a5e577ebb8a3cc3', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='modelsshown',
            name='md5',
            field=models.CharField(default=b'e91cee61ba9d0ec9d2759f59782a292a', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='trim',
            name='md5',
            field=models.CharField(default=b'61020dada3bc0a9a6406fe00e9ceb36e', max_length=255, editable=False),
        ),
    ]
