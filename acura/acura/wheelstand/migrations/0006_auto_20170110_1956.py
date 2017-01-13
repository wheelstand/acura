# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheelstand', '0005_auto_20170110_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exteriorcolour',
            name='md5',
            field=models.CharField(default=b'3e07396650a670124dfeb6d2f526f767', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='md5',
            field=models.CharField(default=b'b424dc1bb6a8e08dceb4c0db88c4679f', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='interiors',
            name='md5',
            field=models.CharField(default=b'b3e51079740f47c6ed7a1d78a0467a39', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='interiors',
            name='url',
            field=models.ImageField(default=b'', upload_to=b'uploads/interiors/', null=True, verbose_name='Image', blank=True),
        ),
        migrations.AlterField(
            model_name='models',
            name='md5',
            field=models.CharField(default=b'4238460f4270c3330031998940022ff6', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='modelsshown',
            name='md5',
            field=models.CharField(default=b'a95a9dc167e49f827a2c55bd52d21d37', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='trim',
            name='md5',
            field=models.CharField(default=b'081a5db40ab0f4eb2d22edbf9bedabf9', max_length=255, editable=False),
        ),
    ]
