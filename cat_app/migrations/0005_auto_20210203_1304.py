# Generated by Django 2.2.5 on 2021-02-03 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat_app', '0004_auto_20210202_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='prod_img',
            field=models.ImageField(blank=True, upload_to='uploads/products/'),
        ),
    ]
