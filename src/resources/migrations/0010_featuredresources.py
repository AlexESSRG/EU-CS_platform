# Generated by Django 2.2.10 on 2020-02-26 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0009_auto_20200221_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Resource')),
            ],
        ),
    ]