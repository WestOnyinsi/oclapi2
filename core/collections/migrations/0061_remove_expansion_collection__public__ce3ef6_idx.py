# Generated by Django 4.1.7 on 2023-04-13 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0060_alter_collection_mnemonic_alter_expansion_mnemonic_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='expansion',
            name='collection__public__ce3ef6_idx',
        ),
    ]