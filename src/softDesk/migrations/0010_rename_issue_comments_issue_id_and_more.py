# Generated by Django 4.2.1 on 2023-06-09 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('softDesk', '0009_alter_contributors_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='issue',
            new_name='issue_id',
        ),
        migrations.RenameField(
            model_name='contributors',
            old_name='project',
            new_name='project_id',
        ),
    ]
