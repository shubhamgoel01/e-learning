# Generated by Django 3.2.5 on 2021-07-17 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0016_diff_digbookmark_diff_digliked_icardsaudiobookmark_icardsaudioliked_icardspdfbookmark_icardspdfliked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='college',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
