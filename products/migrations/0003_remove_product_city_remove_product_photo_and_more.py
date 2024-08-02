# Generated by Django 4.2.1 on 2024-08-02 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_city_product_photo_delete_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='city',
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo',
        ),
        migrations.AddField(
            model_name='product',
            name='cities',
            field=models.ManyToManyField(blank=True, related_name='products', to='products.city'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='products.city')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='products.product')),
            ],
        ),
    ]