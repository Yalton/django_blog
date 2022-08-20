# Generated by Django 4.1 on 2022-08-20 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0018_tutorialfield_remove_tutorial_f1_m0_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorialfieldmedia',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tutorialfieldmedia',
            name='field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='my_app.tutorialfield'),
        ),
    ]
