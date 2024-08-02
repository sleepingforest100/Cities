from django.db import migrations

def fix_null_urls(apps, schema_editor):
    Photo = apps.get_model('products', 'Photo')
    for photo in Photo.objects.filter(url__isnull=True):
        photo.url = 'https://c4.wallpaperflare.com/wallpaper/670/164/913/bow-cake-cream-happy-birthday-wallpaper-preview.jpg'  
        photo.save()

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_photo_url'),  
    ]

    operations = [
        migrations.RunPython(fix_null_urls),
    ]
