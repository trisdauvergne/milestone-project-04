# Generated by Django 3.0.6 on 2020-05-16 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20200515_1057'),
        ('checkout', '0005_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.RegisteredUserProfile'),
        ),
    ]
