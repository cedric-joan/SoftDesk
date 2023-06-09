# Generated by Django 4.2.1 on 2023-05-15 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('softDesk', '0002_remove_projects_author_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('C', 'Create'), ('R', 'Read'), ('CR', 'Create/Read'), ('CRUD', 'Create/Read/Update/Delete')], max_length=4)),
                ('role', models.CharField(choices=[('A', 'Author'), ('C', 'Contributor')], max_length=11)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='softDesk.projects')),
            ],
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('desc', models.TextField(max_length=512)),
                ('tag', models.CharField(choices=[('B', 'Bug'), ('M', 'Maintenance'), ('U', 'Upgrade')], max_length=1)),
                ('priority', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], default='L', max_length=5)),
                ('status', models.CharField(choices=[('T', 'TBD'), ('A', 'Assigned'), ('C', 'Close')], default='T', max_length=8)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('assignee_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='softDesk.contributors')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='softDesk.projects')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=512)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='softDesk.issues')),
            ],
        ),
    ]
