# Generated by Django 4.1.3 on 2022-12-03 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_options_and_more'),
        ('projects', '0004_alter_review_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.profile'),
        ),
    ]
