# Generated by Django 4.1.3 on 2022-12-03 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_skill_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Developer Profile', 'verbose_name_plural': 'Developer Profiles'},
        ),
    ]
