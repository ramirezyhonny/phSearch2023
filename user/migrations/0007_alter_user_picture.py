# Generated by Django 4.2.4 on 2023-10-20 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_rename_province_user_provinces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(default='defaultprofile.svg', upload_to='media'),
        ),
    ]