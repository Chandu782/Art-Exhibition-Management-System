# Generated by Django 5.0.6 on 2024-05-29 06:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artapp', '0007_enquiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='enquiry_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='message',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='mobnum',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='remark',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='remark_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='status',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='fullname',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
