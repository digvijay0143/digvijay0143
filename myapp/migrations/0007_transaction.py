# Generated by Django 4.1.3 on 2022-12-09 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('order_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('checksum', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]