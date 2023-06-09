# Generated by Django 4.2 on 2023-05-13 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(blank=True, max_length=10, null=True)),
                ('order_price', models.IntegerField(blank=True, max_length=10, null=True)),
                ('order_discount', models.IntegerField(blank=True, max_length=10, null=True)),
                ('order_quantity', models.IntegerField(blank=True, max_length=10, null=True)),
                ('order_address', models.IntegerField(blank=True, max_length=10, null=True)),
                ('order_place_at', models.DateField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='students',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')]),
        ),
    ]
