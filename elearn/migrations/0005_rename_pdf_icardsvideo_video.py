# Generated by Django 3.2.5 on 2021-07-09 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0004_auto_20210708_2202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='icardsvideo',
            old_name='pdf',
            new_name='video',
        ),
    ]