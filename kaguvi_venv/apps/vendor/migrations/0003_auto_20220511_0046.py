# Generated by Django 3.1.7 on 2022-05-10 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_vendorprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorprofile',
            name='vendor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor'),
        ),
        migrations.AlterField(
            model_name='vendorprofile',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
    ]
