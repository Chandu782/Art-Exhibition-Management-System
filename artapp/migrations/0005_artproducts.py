# Generated by Django 5.0.6 on 2024-05-27 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artapp', '0004_artmedium_arttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artproducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencenumber', models.IntegerField(default=0, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('images', models.ImageField(upload_to='artpics/images')),
                ('image1', models.ImageField(upload_to='artpics/images')),
                ('image2', models.ImageField(upload_to='artpics/images')),
                ('image3', models.ImageField(upload_to='artpics/images')),
                ('image4', models.ImageField(upload_to='artpics/images')),
                ('dimension', models.CharField(max_length=250)),
                ('orientation', models.CharField(max_length=250)),
                ('size', models.CharField(max_length=250)),
                ('sellingprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artproducts', to='artapp.artist')),
                ('artmedium', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artproducts', to='artapp.artmedium')),
                ('arttype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artproducts', to='artapp.arttype')),
            ],
        ),
    ]
