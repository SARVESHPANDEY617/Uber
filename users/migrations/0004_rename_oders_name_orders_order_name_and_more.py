# Generated by Django 4.2 on 2023-06-02 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_orders_order_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='oders_name',
            new_name='order_name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='oders_address',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='oders_discount',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='oders_place_at',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='oders_quantity',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='oders_time',
        ),
        migrations.RemoveField(
            model_name='students',
            name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='studentsaddress',
            name='pin_code',
        ),
        migrations.RemoveField(
            model_name='studentsaddress',
            name='street_address',
        ),
        migrations.AddField(
            model_name='orders',
            name='discount',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_address',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_at',
            field=models.DateField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_price',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='quanity_of_order',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='mobile',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='studentsaddress',
            name='pincode',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='studentsaddress',
            name='street_name',
            field=models.CharField(blank=True, max_length=19, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='birth',
            field=models.DateField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='first_name',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='gender',
            field=models.IntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'other')]),
        ),
        migrations.AlterField(
            model_name='students',
            name='last_name',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='studentsaddress',
            name='city',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='studentsaddress',
            name='country',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentsaddress',
            name='house_number',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='studentsaddress',
            name='state',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentsaddress',
            name='students',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_addresses', to='users.students'),
        ),
    ]
