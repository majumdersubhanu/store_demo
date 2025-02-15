# Generated by Django 5.1.5 on 2025-02-05 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=2083)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'QR Code',
                'verbose_name_plural': 'QR Codes',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='qr_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.qr'),
        ),
    ]
