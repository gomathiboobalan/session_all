# Generated by Django 2.2.5 on 2021-02-02 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat_app', '0003_auto_20210202_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='prod_img',
            field=models.ImageField(blank=True, upload_to='products/'),
        ),
    ]
