# Generated by Django 3.0.4 on 2020-05-14 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sangha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dhamma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('image', models.URLField(blank=True, default='')),
                ('record_date', models.DateField(blank=True, null=True)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('sadhu', models.IntegerField(blank=True, null=True)),
                ('categories', models.ManyToManyField(to='dhamma.Category')),
                ('language', models.ManyToManyField(to='dhamma.Language')),
                ('location', models.ManyToManyField(to='dhamma.Location')),
                ('media_type', models.ManyToManyField(to='dhamma.MediaType')),
                ('sangha_name', models.ManyToManyField(to='dhamma.Sangha')),
            ],
        ),
    ]
