# Generated by Django 3.1.6 on 2021-03-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0014_remove_comment_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
