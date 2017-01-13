# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheelstand', '0009_auto_20170112_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='engines',
            name='engine_en',
            field=models.CharField(help_text='English', max_length=255, null=True, verbose_name='Name English', blank=True),
        ),
        migrations.AddField(
            model_name='engines',
            name='engine_fr',
            field=models.CharField(help_text='French', max_length=255, null=True, verbose_name='Name French', blank=True),
        ),
        migrations.AlterField(
            model_name='engines',
            name='compressionRatio',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Compression Ratio', blank=True),
        ),
        migrations.AlterField(
            model_name='engines',
            name='idelStop',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Idle Stop', blank=True),
        ),
        migrations.AlterField(
            model_name='exteriorcolour',
            name='md5',
            field=models.CharField(default=b'fe4ecfd381c76ec50b828ef9b4bae531', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='md5',
            field=models.CharField(default=b'192d42ed0c1dcf63fb40c6758c2bb38f', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='interiors',
            name='md5',
            field=models.CharField(default=b'd136153aa9cbd28146111a4deda54e13', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='models',
            name='md5',
            field=models.CharField(default=b'b4292947d7494a24d6a2f9c3816adafc', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='modelsshown',
            name='md5',
            field=models.CharField(default=b'29b204fa7da667c81a3b608bd1994705', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='trim',
            name='md5',
            field=models.CharField(default=b'082b2d14c7618307c4c1404fb8376c94', max_length=255, editable=False),
        ),
    ]
