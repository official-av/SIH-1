# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 04:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=5000)),
                ('subject', models.CharField(max_length=2000)),
                ('type', models.CharField(max_length=500)),
                ('timestamp', models.DateField()),
                ('is_recommended', models.BooleanField(default=False)),
                ('asked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionFor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(null=True)),
                ('asked_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Department')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommeded_answer', models.TextField(max_length=5000)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommeded_by_me', to='portal.Department')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Question')),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommeded_to_me', to='portal.Department')),
            ],
        ),
    ]
