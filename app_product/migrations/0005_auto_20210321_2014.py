# Generated by Django 3.1.7 on 2021-03-21 14:14

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0004_galleryimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='details',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
