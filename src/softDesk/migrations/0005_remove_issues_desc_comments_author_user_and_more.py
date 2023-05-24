# Generated by Django 4.2.1 on 2023-05-23 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('softDesk', '0004_alter_comments_issue_alter_contributors_project_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issues',
            name='desc',
        ),
        migrations.AddField(
            model_name='comments',
            name='author_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contributors',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issues',
            name='author_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projects',
            name='author_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='description',
            field=models.TextField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='comments',
            name='issue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='softDesk.issues'),
        ),
        migrations.AlterField(
            model_name='issues',
            name='assignee_user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='softDesk.contributors'),
        ),
        migrations.AlterField(
            model_name='issues',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue', to='softDesk.projects'),
        ),
    ]