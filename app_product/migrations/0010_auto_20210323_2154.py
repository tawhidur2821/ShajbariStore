# Generated by Django 3.1.6 on 2021-03-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0009_auto_20210323_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
