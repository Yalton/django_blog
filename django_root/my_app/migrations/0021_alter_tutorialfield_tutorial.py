# Generated by Django 4.1 on 2022-08-20 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0020_alter_tutorialfield_tutorial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialfield',
            name='tutorial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='my_app.tutorial'),
        ),
    ]
