# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('internal_id', models.CharField(max_length=16, unique=True)),
                ('group', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('uri', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('doc', models.ForeignKey(to='app.Document')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lang',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrgUnit',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='document',
            name='lang',
            field=models.ForeignKey(to='app.Lang'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='document',
            name='orgunit',
            field=models.ForeignKey(to='app.OrgUnit'),
            preserve_default=True,
        ),
    ]
