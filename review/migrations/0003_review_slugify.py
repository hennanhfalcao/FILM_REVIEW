# Generated by Django 5.1.5 on 2025-01-17 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_rename_author_id_review_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='slugify',
            field=models.SlugField(default='titulo-padrao', max_length=200, unique_for_date='published_at'),
            preserve_default=False,
        ),
    ]
