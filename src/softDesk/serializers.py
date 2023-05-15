from rest_framework import serializers
from .models import Projects, Contributors, Comments, Issues

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class ContributorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = '__all__'            