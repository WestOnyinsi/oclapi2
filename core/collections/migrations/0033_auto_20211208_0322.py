# Generated by Django 3.2.8 on 2021-12-08 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0032_merge_20211126_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='autoexpand',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='autoexpand_head',
            field=models.BooleanField(default=True, null=True),
        ),
    ]