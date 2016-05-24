# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TutorProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default=b'dev', max_length=30, verbose_name=b'User_Name')),
                ('password', models.CharField(default=b'dev', max_length=20)),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('age', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'TutorProfile',
                'verbose_name_plural': "TutorProfile's",
            },
        ),
    ]
