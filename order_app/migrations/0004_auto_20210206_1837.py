# Generated by Django 2.2.5 on 2021-02-06 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0003_auto_20210206_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdb',
            name='prod_itm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='cat_app.Products'),
        ),
    ]
