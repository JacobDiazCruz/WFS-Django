# Generated by Django 2.1.2 on 2018-10-31 12:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181030_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='skills',
        ),
        migrations.AddField(
            model_name='profile',
            name='degree',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='caption',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(max_length=120),
        ),
    ]
