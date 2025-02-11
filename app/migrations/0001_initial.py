# Generated by Django 5.1.6 on 2025-02-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('length', models.IntegerField()),
                ('review', models.TextField()),
                ('rating', models.FloatField()),
                ('date_watched', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
