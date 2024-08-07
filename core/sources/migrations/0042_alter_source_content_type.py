# Generated by Django 4.2.4 on 2024-05-09 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0041_source_source_org_released_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='content_type',
            field=models.TextField(blank=True, choices=[('not-present', 'not-present'), ('example', 'example'), ('fragment', 'fragment'), ('complete', 'complete'), ('supplement', 'supplement')], null=True),
        ),
    ]
