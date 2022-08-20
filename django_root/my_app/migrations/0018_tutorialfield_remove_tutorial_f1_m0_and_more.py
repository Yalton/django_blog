# Generated by Django 4.1 on 2022-08-20 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0017_remove_article_typeslug_remove_service_typeslug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorialField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_title', models.CharField(blank=True, max_length=100, null=True)),
                ('field_content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f1_m0',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f1_m1',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f1_m2',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f1_m3',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f1_m4',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f1_m5',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f2_m0',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f2_m1',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f2_m2',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f2_m3',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f2_m4',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f2_m5',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f3_m0',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f3_m1',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f3_m2',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f3_m3',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f3_m4',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f3_m5',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f4_m0',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f4_m1',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f4_m2',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f4_m3',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f4_m4',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f4_m5',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f5_m0',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f5_m1',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f5_m2',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f5_m3',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f5_m4',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f5_m5',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f6_m0',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f6_m1',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f6_m2',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f6_m3',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f6_m4',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='f6_m5',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='field1_content',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='field1_reqd',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='field1_title',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='field2_content',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='field2_reqd',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='field2_title',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='field3_content',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='field3_reqd',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='field3_title',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='field4_content',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='field4_reqd',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='field4_title',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='field5_content',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='field5_reqd',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='field5_title',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='field6_content',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='field6_reqd',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='field6_title',
        ),
        migrations.CreateModel(
            name='TutorialFieldMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media0', models.ImageField(blank=True, null=True, upload_to='uploads/tutorials/%Y/%m/%d/')),
                ('field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.tutorialfield')),
            ],
        ),
        migrations.AddField(
            model_name='tutorialfield',
            name='tutorial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.tutorial'),
        ),
    ]
