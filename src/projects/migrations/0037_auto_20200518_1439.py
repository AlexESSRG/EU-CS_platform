# Generated by Django 2.2.10 on 2020-05-18 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0036_project_top'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredprojects',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]
