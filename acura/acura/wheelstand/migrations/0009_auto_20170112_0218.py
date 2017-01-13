# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheelstand', '0008_auto_20170112_0217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='engines',
            old_name='compression',
            new_name='compressionRatio',
        ),
        migrations.AlterField(
            model_name='exteriorcolour',
            name='md5',
            field=models.CharField(default=b'90aa1d54ac69ef0c478fcbd23ec9d729', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='md5',
            field=models.CharField(default=b'4fa45db2b7630afeed5f59c3006e097e', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='interiors',
            name='md5',
            field=models.CharField(default=b'27ed71dd9120f96b43d648704fab91a9', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='models',
            name='md5',
            field=models.CharField(default=b'a1a15403ef17972f437a0ff707faa62f', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='modelsshown',
            name='md5',
            field=models.CharField(default=b'02ed25d1448e6ade50df99d66134c83c', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='trim',
            name='md5',
            field=models.CharField(default=b'9edbc08215b3f40e312ea5d2f9b15b6e', max_length=255, editable=False),
        ),
    ]
