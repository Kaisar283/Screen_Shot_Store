# Generated by Django 4.0.5 on 2022-06-07 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=30)),
                ('discription', models.TextField(blank=True)),
            ],
        ),
    ]