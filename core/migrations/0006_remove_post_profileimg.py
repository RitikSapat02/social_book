# Generated by Django 4.0.6 on 2023-05-11 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_post_profileimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='profileimg',
        ),
    ]