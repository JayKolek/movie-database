# Generated by Django 2.0.2 on 2019-01-10 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('title',)},
        ),
    ]
