# Generated by Django 5.1.4 on 2024-12-29 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_annualreport_annualreport_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='director_image',
        ),
    ]
