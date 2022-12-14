# Generated by Django 4.1 on 2022-08-26 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('by', models.CharField(max_length=50)),
                ('time', models.IntegerField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('dead', models.BooleanField(default=False)),
                ('text', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('descendants', models.IntegerField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('parent', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('polls', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='part', to='news.item')),
            ],
        ),
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kid', to='news.item')),
            ],
        ),
    ]
