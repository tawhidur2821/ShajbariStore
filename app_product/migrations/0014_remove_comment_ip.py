# Generated by Django 3.1.6 on 2021-03-25 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0013_remove_comment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='ip',
        ),
    ]
