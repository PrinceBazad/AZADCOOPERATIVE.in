# Generated by Django 5.1.4 on 2024-12-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_homeslide_aboutlong_alter_homeslide_aboutshort'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeslide',
            name='Registrationnumber',
            field=models.CharField(default='MSCS/CR/208/2005', max_length=20),
        ),
    ]
