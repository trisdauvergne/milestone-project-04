# Generated by Django 3.0.6 on 2020-05-14 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20200513_1001'),
        ('prints', '0002_auto_20200511_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='print',
            name='designer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.DesignerProfile'),
        ),
    ]