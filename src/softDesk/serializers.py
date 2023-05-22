from rest_framework import serializers
from .models import Projects, Contributors, Comments, Issues

class ProjectsSerializer(serializers.ModelSerializer):

    issue = serializers.SerializerMethodField()
    class Meta:
        model = Projects
        fields = ['id', 'title', 'description', 'type', 'contributor', 'issue']


class ContributorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = ['id', 'project', 'role', 'permission']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'description', ]


class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = ['id', 'title', 'tag', 'priority', 'project']            