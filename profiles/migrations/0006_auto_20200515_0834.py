# Generated by Django 3.0.6 on 2020-05-15 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_designerprofile_register_designer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designerprofile',
            name='register_designer',
            field=models.BooleanField(),
        ),
    ]