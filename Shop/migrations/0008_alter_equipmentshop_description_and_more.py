# Generated by Django 5.2.4 on 2025-07-21 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0007_equipmentshop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentshop',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='manshop',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='womenshop',
            name='description',
            field=models.TextField(),
        ),
    ]
