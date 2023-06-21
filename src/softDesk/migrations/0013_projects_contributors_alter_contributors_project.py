# Generated by Django 4.2.1 on 2023-06-14 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('softDesk', '0012_rename_issue_id_comments_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='contributors',
            field=models.ManyToManyField(related_name='project', through='softDesk.Contributors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contributors',
            name='project',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='softDesk.projects'),
        ),
    ]