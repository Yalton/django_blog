# Generated by Django 4.1 on 2022-08-20 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_alter_article_options_alter_service_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='tutorial',
            options={},
        ),
        migrations.RemoveField(
            model_name='service',
            name='references',
        ),
        migrations.RemoveField(
            model_name='service',
            name='sub_title',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='references',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='sub_title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
