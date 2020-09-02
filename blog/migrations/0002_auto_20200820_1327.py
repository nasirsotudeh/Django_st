# Generated by Django 3.0.5 on 2020-08-20 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='titleCategory')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='TitleSlug')),
                ('status', models.BooleanField(default=True, verbose_name='show?')),
                ('position', models.IntegerField(verbose_name='position')),
            ],
            options={
                'verbose_name': 'title',
                'verbose_name_plural': 'titles',
                'ordering': ['position'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(default=2, upload_to='media'),
            preserve_default=False,
        ),
    ]
