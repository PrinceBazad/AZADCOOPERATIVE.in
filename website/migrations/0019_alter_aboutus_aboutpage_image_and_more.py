# Generated by Django 5.1.4 on 2024-12-28 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_aboutus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='Aboutpage_image',
            field=models.ImageField(default='', upload_to='website/Aboutpage/images/mainimage'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='Aboutpage_visionimage',
            field=models.ImageField(default='', upload_to='website/Aboutpage/images/visionimage'),
        ),
    ]
