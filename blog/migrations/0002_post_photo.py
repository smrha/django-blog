# Generated by Django 4.2.5 on 2023-09-16 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='posts/%Y/%m/%d'),
        ),
    ]
