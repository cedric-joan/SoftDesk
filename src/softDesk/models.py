from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL


class Projects(models.Model):
    PROJECT_TYPES = [
        ('B', 'Back-end'),
        ('F', 'Front-end'),
        ('I', 'IOS'),
        ('A', 'Android'),
    ]
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=512)
    type = models.CharField(choices=PROJECT_TYPES, max_length=9)
    author_user_id = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'[Projects:{self.id} {self.title}]'
    

class Contributors(models.Model):
    CONTRIBUTOR_PERMISSIONS = [
        ('C', "Create"),
        ('R', "Read"),
        ('CR', "Create/Read"),
        ('CRUD', "Create/Read/Update/Delete"),
    ]

    CONTRIBUTOR_ROLES = [
        ('A', 'Author'),
        ('C', 'Contributor')
    ]

    user = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(to=Projects, on_delete=models.CASCADE, related_name="contributor")
    permission = models.CharField(max_length=4, choices=CONTRIBUTOR_PERMISSIONS)
    role = models.CharField(max_length=11, choices=CONTRIBUTOR_ROLES)

    def __str__(self) -> str:
        return f'[Contributors:{self.id} {self.user}]'
    
class Issues(models.Model):
    ISSUE_TAGS = [
        ('B', 'Bug'),
        ('T', 'Task'),
        ('U', 'Upgrade')
    ]

    ISSUE_PRIORITIES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High')
    ]

    ISSUE_STATUSES = [
        ('I', 'InProgress'),
        ('T', 'ToDo'),
        ('C', 'Close')
    ]
    title = models.CharField(max_length=64)
    # description = models.TextField(max_length=512, blank=True)
    tag = models.CharField(choices=ISSUE_TAGS, max_length=1)
    project = models.ForeignKey(to=Projects, on_delete=models.CASCADE, related_name="issue")
    priority = models.CharField(choices=ISSUE_PRIORITIES, max_length=45, default='L')
    status = models.CharField(choices=ISSUE_STATUSES, max_length=45, default='T')
    author_user_id = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    assignee_user = models.ForeignKey(to=Contributors, on_delete=models.CASCADE, blank=True)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        issue_id = f'[Issues:{self.id} {self.title}]'
        return issue_id


class Comments(models.Model):
    description = models.TextField(max_length=512, blank=True)
    author_user_id = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    issue = models.ForeignKey(to=Issues, on_delete=models.CASCADE, related_name="comment", null=True)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[Comments:{self.id} {self.issue}]'    