# Generated by Django 4.2.1 on 2024-08-02 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_fix_null_urls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='url',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cities',
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(default='photos/default.jpg', upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='photo',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photos', to='products.city'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]