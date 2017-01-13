# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import colorfield.fields
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_en', models.CharField(help_text='English', max_length=255, verbose_name='Name English')),
                ('name_fr', models.CharField(help_text='French', max_length=255, null=True, verbose_name='Name French', blank=True)),
                ('base_price', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Accessories',
            },
        ),
        migrations.CreateModel(
            name='Colours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='English', max_length=255, verbose_name='name')),
                ('hexcode', colorfield.fields.ColorField(default=b'#FFFFFF', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Colours',
            },
        ),
        migrations.CreateModel(
            name='Engines',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_en', models.CharField(help_text='English', max_length=255, verbose_name='Name English')),
                ('name_fr', models.CharField(help_text='French', max_length=255, null=True, verbose_name='Name French', blank=True)),
                ('hp', models.CharField(max_length=255, null=True, blank=True)),
                ('torque', models.CharField(max_length=255, null=True, blank=True)),
                ('displacement', models.CharField(max_length=255, null=True, blank=True)),
                ('emissions_en', models.CharField(help_text='English', max_length=255, null=True, verbose_name='Emissions English', blank=True)),
                ('emissions_fr', models.CharField(help_text='French', max_length=255, null=True, verbose_name='Emissions French', blank=True)),
                ('bore_and_stroke_en', models.CharField(help_text='English', max_length=255, null=True, verbose_name='Bore and Stroke English', blank=True)),
                ('bore_and_stroke_fr', models.CharField(help_text='French', max_length=255, null=True, verbose_name='Bore and Stroke French', blank=True)),
                ('compression', models.CharField(max_length=255, null=True, blank=True)),
                ('driveByWire', models.BooleanField(max_length=255, verbose_name='Drive-by-Wire Throttle System')),
                ('ecoAssis', models.BooleanField(max_length=255)),
                ('recommended_fuel_en', models.CharField(help_text='English', max_length=255, null=True, verbose_name='Recommended fuel English', blank=True)),
                ('recommended_fuel_fr', models.CharField(help_text='French', max_length=255, null=True, verbose_name='Recommended fuel French', blank=True)),
                ('twoLiter', models.BooleanField(default=False)),
                ('onePointFiveLiter', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Engines',
            },
        ),
        migrations.CreateModel(
            name='ExteriorColour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('colour', colorfield.fields.ColorField(default=b'#FFFFFF', max_length=10)),
                ('selected', models.BooleanField(default=False)),
                ('url', models.ImageField(upload_to=b'uploads/trim_exterior_colour/', null=True, verbose_name='Image', blank=True)),
                ('link', models.CharField(max_length=255, null=True, verbose_name='OR Remote URL', blank=True)),
                ('md5', models.CharField(default=b'e70bfddeec2b8006db8947e680715609', max_length=255, editable=False)),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, editable=False, monitor=b'url')),
            ],
            options={
                'verbose_name_plural': 'Exterior Colour',
            },
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_en', models.CharField(max_length=255, verbose_name='Features English')),
                ('name_fr', models.CharField(max_length=255, verbose_name='Features French')),
            ],
            options={
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.ImageField(upload_to=b'uploads/gallery/', null=True, verbose_name='Image', blank=True)),
                ('link', models.CharField(max_length=255, null=True, verbose_name='OR Remote URL', blank=True)),
                ('md5', models.CharField(default=b'fffd9e82f01d4e82e2523ee4046b2d17', max_length=255, editable=False)),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, editable=False, monitor=b'url')),
            ],
            options={
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.CreateModel(
            name='InteriorColour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255)),
                ('colour', colorfield.fields.ColorField(default=b'#FFFFFF', max_length=10)),
                ('selected', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Interior Colour',
            },
        ),
        migrations.CreateModel(
            name='Interiors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('url', models.ImageField(upload_to=b'uploads/interiors/', null=True, verbose_name='Image', blank=True)),
                ('link', models.CharField(max_length=255, null=True, verbose_name='OR Remote URL', blank=True)),
                ('md5', models.CharField(default=b'f3957160e08fbb6f8166a8633be09c60', max_length=255, editable=False)),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, editable=False, monitor=b'url')),
            ],
            options={
                'verbose_name_plural': 'Interiors',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='English', max_length=255, verbose_name='name')),
                ('language', models.CharField(default=b'EN', max_length=4, choices=[(b'EN', b'English'), (b'FR', b'French')])),
            ],
            options={
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Models',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_en', models.CharField(help_text='English', max_length=255, verbose_name=b'Name English')),
                ('name_fr', models.CharField(help_text='French', max_length=255, null=True, verbose_name=b'Name French', blank=True)),
                ('year', models.CharField(max_length=4, choices=[(b'2013', b'2013'), (b'2014', b'2014'), (b'2015', b'2015'), (b'2016', b'2016'), (b'2017', b'2017'), (b'2018', b'2018'), (b'2019', b'2019'), (b'2020', b'2020')])),
                ('subhead_en', models.TextField(help_text='English', max_length=2550, null=True, verbose_name=b'Subhead English', blank=True)),
                ('subhead_fr', models.TextField(help_text='French', max_length=2550, null=True, verbose_name=b'Subhead French', blank=True)),
                ('url', models.ImageField(upload_to=b'uploads/models/', null=True, verbose_name='Hero Image', blank=True)),
                ('link', models.CharField(max_length=255, null=True, verbose_name=b'OR Remote URL', blank=True)),
                ('disclaimer_en', models.TextField(help_text='English', max_length=500, null=True, verbose_name=b'Disclaimer English', blank=True)),
                ('disclaimer_fr', models.TextField(help_text='French', max_length=500, null=True, verbose_name=b'Disclaimer French', blank=True)),
                ('base_price', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('freight_DPI', models.DecimalField(null=True, verbose_name=b'Freight & DPI', max_digits=8, decimal_places=2, blank=True)),
                ('special_offers', models.CharField(max_length=255)),
                ('line1_en', models.CharField(help_text='English', max_length=255, null=True, verbose_name=b'Line 1 English', blank=True)),
                ('line1_fr', models.CharField(help_text='French', max_length=255, null=True, verbose_name=b'Line 1 French', blank=True)),
                ('line2_en', models.CharField(help_text='English', max_length=255, null=True, verbose_name=b'Line 2 English', blank=True)),
                ('line2_fr', models.CharField(help_text='French', max_length=255, null=True, verbose_name=b'Line 2 French', blank=True)),
                ('percentage', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('price', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('md5', models.CharField(default=b'd198f2842f7a7651def9cad5431ae2f6', max_length=255, editable=False)),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, editable=False, monitor=b'url')),
            ],
            options={
                'verbose_name_plural': 'Models',
            },
        ),
        migrations.CreateModel(
            name='ModelsShown',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wheels_en', models.CharField(help_text='English', max_length=255, null=True, blank=True)),
                ('wheels_fr', models.CharField(help_text='French', max_length=255, null=True, blank=True)),
                ('drivetrain', models.CharField(blank=True, max_length=4, null=True, choices=[(b'AUT', b'Automtic'), (b'MAN', b'Manual'), (b'FRW', b'Front-wheel'), (b'FOW', b'Four-wheel')])),
                ('price_override', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('accessory', models.ForeignKey(blank=True, to='wheelstand.Accessories', null=True)),
                ('location', models.ManyToManyField(to='wheelstand.Location', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Models Shown',
            },
        ),
        migrations.CreateModel(
            name='Transmissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_en', models.CharField(help_text='English', max_length=255, verbose_name='Name English')),
                ('name_fr', models.CharField(help_text='French', max_length=255, null=True, verbose_name='Name French', blank=True)),
                ('abberviation', models.CharField(max_length=255, null=True, verbose_name='Abbreviation', blank=True)),
                ('selected', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Transmissions',
            },
        ),
        migrations.CreateModel(
            name='Trim',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_en', models.CharField(help_text='English', max_length=255, verbose_name=b'Name English')),
                ('name_fr', models.CharField(help_text='French', max_length=255, null=True, verbose_name=b'Name French', blank=True)),
                ('url', models.ImageField(upload_to=b'uploads/interiors/', null=True, verbose_name='Image', blank=True)),
                ('link', models.CharField(max_length=255, null=True, verbose_name='OR Remote URL', blank=True)),
                ('md5', models.CharField(default=b'4c6956d27c2a93c59e8ab54849925adb', max_length=255, editable=False)),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, editable=False, monitor=b'url')),
                ('heading_en', models.CharField(help_text='English', max_length=255, verbose_name=b'Heading English')),
                ('heading_fr', models.CharField(help_text='French', max_length=255, null=True, verbose_name=b'Heading French', blank=True)),
                ('description_en', models.TextField(help_text='English', max_length=2000, verbose_name=b'Description English')),
                ('description_fr', models.TextField(help_text='French', max_length=2000, null=True, verbose_name=b'Description French', blank=True)),
                ('base_price', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('fuel_city', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('fuel_highway', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('fuel_combined', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('highlights_en', models.CharField(help_text='English', max_length=2000, null=True, verbose_name=b'Highlights English', blank=True)),
                ('highlights_fr', models.CharField(help_text='French', max_length=2000, null=True, verbose_name=b'Highlights French', blank=True)),
                ('colour', models.ForeignKey(blank=True, to='wheelstand.Colours', null=True)),
                ('engine', models.ForeignKey(blank=True, to='wheelstand.Engines', null=True)),
                ('features', models.ManyToManyField(to='wheelstand.Features', blank=True)),
                ('interiors', models.ManyToManyField(to='wheelstand.Interiors', blank=True)),
                ('model', models.ForeignKey(blank=True, to='wheelstand.Models', null=True)),
                ('transmission', models.ForeignKey(blank=True, to='wheelstand.Transmissions', null=True)),
            ],
            options={
                'verbose_name_plural': 'Trims',
            },
        ),
        migrations.AddField(
            model_name='modelsshown',
            name='trim',
            field=models.ForeignKey(blank=True, to='wheelstand.Trim', null=True),
        ),
        migrations.AddField(
            model_name='modelsshown',
            name='vehicle',
            field=models.ForeignKey(blank=True, to='wheelstand.Models', null=True),
        ),
        migrations.AddField(
            model_name='interiorcolour',
            name='trim_interior_colour',
            field=models.ForeignKey(related_name='interiorColours', blank=True, to='wheelstand.Trim', null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ForeignKey(blank=True, to='wheelstand.Models', null=True),
        ),
        migrations.AddField(
            model_name='exteriorcolour',
            name='trim_exterior_colour',
            field=models.ForeignKey(related_name='exteriorColours', blank=True, to='wheelstand.Trim', null=True),
        ),
    ]
