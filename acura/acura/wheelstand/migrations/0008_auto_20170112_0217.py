# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheelstand', '0007_auto_20170112_0203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engines',
            name='hp',
        ),
        migrations.AddField(
            model_name='engines',
            name='horsePower',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Horsepower', blank=True),
        ),
        migrations.AlterField(
            model_name='engines',
            name='activeControl',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Active Control', blank=True),
        ),
        migrations.AlterField(
            model_name='engines',
            name='hyBridPowerTrain',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Hybrid Powertrain', blank=True),
        ),
        migrations.AlterField(
            model_name='engines',
            name='hybridHorsePower',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Hybrid Horsepower', blank=True),
        ),
        migrations.AlterField(
            model_name='engines',
            name='hybridTorque',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Hybrid Torque', blank=True),
        ),
        migrations.AlterField(
            model_name='engines',
            name='idelStop',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Active Control', blank=True),
        ),
        migrations.AlterField(
            model_name='engines',
            name='vcm',
            field=models.CharField(max_length=255, null=True, verbose_name=b'VCM', blank=True),
        ),
        migrations.AlterField(
            model_name='exteriorcolour',
            name='md5',
            field=models.CharField(default=b'acaeefbb6d5446eb90b3643944069b62', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='md5',
            field=models.CharField(default=b'cb05d4a1ff2b8e1c09954001b67dfc0b', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='interiors',
            name='md5',
            field=models.CharField(default=b'ab4fbfa5ef04ac5b0dc591998eb8c0a5', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='models',
            name='md5',
            field=models.CharField(default=b'110a4ac4d42a48182b8f6a6565554b2b', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='modelsshown',
            name='md5',
            field=models.CharField(default=b'dfbd4e21d4d3d4f59c357cbf1809ccd5', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='trim',
            name='md5',
            field=models.CharField(default=b'fe3b6ffef946e9b5fe0a73c0a8402912', max_length=255, editable=False),
        ),
    ]
