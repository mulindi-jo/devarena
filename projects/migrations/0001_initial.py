# Generated by Django 4.1.3 on 2022-11-26 22:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_archived', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('demo_link', models.TextField(blank=True, max_length=2000, null=True)),
                ('source_link', models.TextField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
