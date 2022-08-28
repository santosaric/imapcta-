# Generated by Django 4.1 on 2022-08-28 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_product_codigo_do_produto"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="foto",
            field=models.ImageField(blank=True, upload_to="fotos/%Y/%m/"),
        ),
        migrations.AlterField(
            model_name="product",
            name="estoque",
            field=models.IntegerField(verbose_name="Quantidade em Estoque"),
        ),
    ]