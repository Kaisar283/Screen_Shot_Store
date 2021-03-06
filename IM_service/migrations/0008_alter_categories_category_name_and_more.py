# Generated by Django 4.0.5 on 2022-06-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IM_service', '0007_alter_sub_categoryes_s_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category_name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='name_store',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='supplier_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
