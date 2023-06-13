# Generated by Django 4.2.1 on 2023-06-01 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softDesk', '0006_rename_author_user_comments_author_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issues',
            old_name='assignee_user',
            new_name='assignee_user_id',
        ),
        migrations.RenameField(
            model_name='issues',
            old_name='project',
            new_name='project_id',
        ),
        migrations.AddField(
            model_name='issues',
            name='description',
            field=models.TextField(blank=True, max_length=512),
        ),
    ]
