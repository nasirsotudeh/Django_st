# Generated by Django 3.0.5 on 2020-09-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200820_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['position'], 'verbose_name': 'Categor', 'verbose_name_plural': 'titles'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='Category',
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='articles', to='blog.Category', verbose_name='categorys'),
        ),
    ]
