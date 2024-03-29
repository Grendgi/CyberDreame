# Generated by Django 4.2.9 on 2024-02-20 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Название')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Контент')),
                ('image', models.ImageField(blank=True, null=True, upload_to='slides/', verbose_name='Изображение')),
                ('order', models.IntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
