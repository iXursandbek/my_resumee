# Generated by Django 3.1.7 on 2021-04-24 10:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutme', models.TextField(max_length=150)),
                ('profession', models.CharField(max_length=50)),
                ('about_profession', ckeditor.fields.RichTextField(max_length=150)),
                ('birthday', models.CharField(default='Aprel 19, 1996', max_length=100, verbose_name='Birthday')),
                ('website', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('degrre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_name_degree', models.CharField(max_length=50)),
                ('about_edu', ckeditor.fields.RichTextField(max_length=254)),
                ('year', models.CharField(default='2014-2019', max_length=254)),
                ('university_name', models.CharField(default='TATU', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Dizayner', max_length=254)),
                ('year', models.CharField(default='2014-2019', max_length=254)),
                ('title', models.CharField(default='IdealSoft MCHJ, Urganch', max_length=254)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=50)),
                ('profession1', models.CharField(max_length=50)),
                ('profession2', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Name')),
                ('percentage', models.CharField(max_length=50, verbose_name='Percentage')),
                ('about_skil', models.CharField(default='mahoratlarim haqida qisqacha', max_length=254)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
                ('city', models.CharField(default='Yangiariq', max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(default='sss@mail.ru', max_length=54)),
                ('year', models.CharField(default='2014-2019', max_length=254)),
            ],
        ),
    ]
