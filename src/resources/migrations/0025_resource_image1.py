# Generated by Django 2.2.10 on 2020-03-21 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0024_resource_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='image1',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
