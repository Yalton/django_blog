# Generated by Django 4.1 on 2022-08-21 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_remove_tutorial_videourl_tutorial_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(blank=True, null=True, upload_to='uploads/personaldata/resume/%Y/%m/%d/')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='sub_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/articles/sub_images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='tutorialfieldcontentmedia',
            name='media',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/tutorials/fieldmedia/%Y/%m/%d/'),
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('summary', models.CharField(blank=True, max_length=300, null=True)),
                ('item_image', models.ImageField(null=True, upload_to='uploads/items/%Y/%m/%d/')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(max_length=100, null=True)),
                ('sub_title', models.TextField(blank=True, null=True)),
                ('references', models.TextField(blank=True, null=True)),
                ('notes', models.FileField(blank=True, null=True, upload_to='uploads/notes/videos/%Y/%m/%d/')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
