from rest_framework.serializers import ModelSerializer
from .models import Projects, Contributors, Comments, Issues

class ProjectsSerializer(ModelSerializer):

    class Meta:
        model = Projects
        fields = "__all__"
        read_only_fields = ('author', 'id')


class ContributorsSerializer(ModelSerializer):

    class Meta:
        model = Contributors
        fields = '__all__'
        read_only__fields = ('project_id', 'role', 'id')


class IssuesSerializer(ModelSerializer):

    class Meta:
        model = Issues
        fields = '__all__'
        read_only__fields = ('project', 'author', 'created_time', 'id')


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        read_only__fields = ('author', 'issue', 'created_time', 'id')