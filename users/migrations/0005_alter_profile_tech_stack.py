# Generated by Django 4.1.3 on 2022-12-03 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_tech_stack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tech_stack',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
