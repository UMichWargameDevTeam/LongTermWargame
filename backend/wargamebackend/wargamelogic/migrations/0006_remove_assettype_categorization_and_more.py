# Generated by Django 5.2.4 on 2025-07-31 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wargamelogic', '0005_asset_created_at_asset_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assettype',
            name='categorization',
        ),
        migrations.AddField(
            model_name='assettype',
            name='classification',
            field=models.CharField(choices=[('LAND', 'Land'), ('SEA', 'Sea'), ('AIR', 'Air')], default='SEA', max_length=10),
            preserve_default=False,
        ),
    ]
