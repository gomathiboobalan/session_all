# Generated by Django 2.2.5 on 2021-02-03 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat_app', '0005_auto_20210203_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='prod_img',
            field=models.ImageField(null=True, upload_to='uploads/products/'),
        ),
    ]
