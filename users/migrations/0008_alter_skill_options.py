# Generated by Django 4.1.3 on 2022-12-03 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_skill_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name': 'Profile Skill', 'verbose_name_plural': 'Profile Skills'},
        ),
    ]