# Generated by Django 4.2.4 on 2023-09-02 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_data', '0006_image_remove_card_image_card_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='image',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]