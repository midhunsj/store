# Generated by Django 4.2.5 on 2023-10-06 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ('name',), 'verbose_name': 'course', 'verbose_name_plural': 'courses'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ('name',), 'verbose_name': 'department', 'verbose_name_plural': 'departments'},
        ),
    ]
