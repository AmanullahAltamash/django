# Generated by Django 5.1.3 on 2024-11-22 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_tag_rename_source_link_table_source_links_table_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='table',
            name='vote_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
