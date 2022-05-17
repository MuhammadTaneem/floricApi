# Generated by Django 3.2.7 on 2022-05-16 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20220515_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_img',
            field=models.ImageField(default='images/floric.jpg', upload_to='images/category/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img1',
            field=models.ImageField(default='images/floric.jpg', upload_to='images/products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img2',
            field=models.ImageField(blank=True, default='images/floric.jpg', null=True, upload_to='images/products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img3',
            field=models.ImageField(blank=True, default='images/floric.jpg', null=True, upload_to='images/products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img4',
            field=models.ImageField(blank=True, default='images/floric.jpg', null=True, upload_to='images/products'),
        ),
    ]