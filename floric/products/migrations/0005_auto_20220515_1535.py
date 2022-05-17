# Generated by Django 3.2.7 on 2022-05-15 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20220515_1000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_img',
            new_name='product_img1',
        ),
        migrations.AddField(
            model_name='product',
            name='product_img2',
            field=models.ImageField(blank=True, default='images/logo.png', null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_img3',
            field=models.ImageField(blank=True, default='images/logo.png', null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_img4',
            field=models.ImageField(blank=True, default='images/logo.png', null=True, upload_to='images/'),
        ),
    ]