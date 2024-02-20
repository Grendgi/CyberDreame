# Generated by Django 4.2.9 on 2024-02-20 21:03

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
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('content_structure', models.JSONField(blank=True, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='news_images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='news_videos/')),
                ('file', models.FileField(blank=True, null=True, upload_to='news_files/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='Publishers.category')),
            ],
        ),
        migrations.CreateModel(
            name='NewsVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='news_videos/')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='Publishers.news')),
            ],
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news_images/')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Publishers.news')),
            ],
        ),
        migrations.CreateModel(
            name='NewsFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='news_files/')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='Publishers.news')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Publishers.news')),
            ],
        ),
    ]
