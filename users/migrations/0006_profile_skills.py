# Generated by Django 2.1.2 on 2018-10-31 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_profile_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.CharField(default=2, max_length=12),
            preserve_default=False,
        ),
    ]
