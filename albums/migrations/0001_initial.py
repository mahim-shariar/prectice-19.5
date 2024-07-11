# Generated by Django 5.0.6 on 2024-07-05 23:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician_directory', '0002_rename_muisian_muisician'),
    ]

    operations = [
        migrations.CreateModel(
            name='album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Album_name', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('Artist_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician_directory.muisician')),
            ],
        ),
    ]
