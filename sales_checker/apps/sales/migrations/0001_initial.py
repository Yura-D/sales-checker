# Generated by Django 3.2 on 2021-05-09 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.URLField(max_length=255)),
                ('xpath', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'sales',
            },
        ),
    ]
