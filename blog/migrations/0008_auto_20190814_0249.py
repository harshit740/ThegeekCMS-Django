# Generated by Django 2.2.3 on 2019-08-14 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-publish_on', '-created_on']},
        ),
    ]
