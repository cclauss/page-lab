# Generated by Django 2.0.8 on 2018-11-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0012_auto_20181113_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='usertimingmeasurename',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]