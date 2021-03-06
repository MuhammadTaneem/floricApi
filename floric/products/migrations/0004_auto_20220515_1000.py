# Generated by Django 3.2.7 on 2022-05-15 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220511_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Model',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ImageField(default='images/logo.png', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=512),
        ),
    ]
