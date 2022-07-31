# Generated by Django 4.0.5 on 2022-06-20 02:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category_image', models.ImageField(null=True, upload_to='uploads/categories/%Y/%m/%d/')),
                ('cat_summary', models.CharField(max_length=300)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('room', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_added',),
            },
        ),
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('summary', models.CharField(default='NULL', max_length=300)),
                ('introduction', models.TextField(default='NULL')),
                ('description', models.TextField(default='NULL')),
                ('s_media0', models.ImageField(null=True, upload_to='uploads/rholes/%Y/%m/%d/')),
                ('s_media1', models.ImageField(null=True, upload_to='uploads/rholes/%Y/%m/%d/')),
                ('s_media2', models.ImageField(null=True, upload_to='uploads/rholes/%Y/%m/%d/')),
                ('s_media3', models.ImageField(null=True, upload_to='uploads/rholes/%Y/%m/%d/')),
                ('s_media4', models.ImageField(null=True, upload_to='uploads/rholes/%Y/%m/%d/')),
                ('s_media5', models.ImageField(null=True, upload_to='uploads/rholes/%Y/%m/%d/')),
                ('references', models.TextField(default='NULL')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.category')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
