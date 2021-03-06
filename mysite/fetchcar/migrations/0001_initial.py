# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=30)),
                ('car_type', models.CharField(max_length=30)),
                ('reg_time', models.DateField()),
                ('mileage', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
