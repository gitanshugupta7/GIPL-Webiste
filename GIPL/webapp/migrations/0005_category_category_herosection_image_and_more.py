# Generated by Django 4.1 on 2023-04-17 08:07

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_query_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_herosection_image',
            field=models.ImageField(default='/static/images/ship.webp', upload_to='category_card_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_herosection_image',
            field=models.ImageField(default='/static/images/ship.webp', upload_to='product_card_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_info_body',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
    ]