# Generated by Django 4.2.4 on 2023-09-02 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_data', '0003_card_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='image',
            field=models.ImageField(default='image.jpg', upload_to=''),
        ),
    ]