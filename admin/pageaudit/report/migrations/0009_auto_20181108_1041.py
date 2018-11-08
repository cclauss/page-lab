# Generated by Django 2.0.8 on 2018-11-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0008_auto_20181108_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchkeyval',
            name='url',
        ),
        migrations.RemoveField(
            model_name='urlpath',
            name='url',
        ),
        migrations.AddField(
            model_name='url',
            name='search_key_vals',
            field=models.ManyToManyField(to='report.SearchKeyVal'),
        ),
        migrations.AddField(
            model_name='url',
            name='url_paths',
            field=models.ManyToManyField(to='report.UrlPath'),
        ),
    ]
