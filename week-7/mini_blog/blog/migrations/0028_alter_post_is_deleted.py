# Generated by Django 4.0.6 on 2022-08-04 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Soft delete'),
        ),
    ]
