# Generated by Django 4.2.1 on 2023-06-12 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('softDesk', '0010_rename_issue_comments_issue_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contributors',
            old_name='project_id',
            new_name='project',
        ),
    ]
