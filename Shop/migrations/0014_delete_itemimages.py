# Generated by Django 5.2.4 on 2025-07-28 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0013_product_remove_itemimageseq_item_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ItemImages',
        ),
    ]
