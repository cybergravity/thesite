# Generated by Django 2.2 on 2020-07-27 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_auto_20200727_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='destination',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='travello.Destination'),
        ),
    ]
