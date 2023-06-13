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

    # def create(self, validated_data):
    #     project_id = get_object_or_404(Projects,id=self.kwargs["pk"])

    #     contributor = Contributors.objects.create(
    #         user=validated_data['user'], project=project_id
    #     )
    #     return contributor

class IssuesSerializer(ModelSerializer):

    class Meta:
        model = Issues
        fields = '__all__'
        read_only__fields = ('project', 'author', 'created_time', 'id')

    # def _user(self):
    #     request = self.context.get("request", None)
    #     if request:
    #         return request.user
        
    # def create(self, validated_data):
    #     project = Projects.objects.get(id=self.context['view'].kwargs['project_pk'])
    #     issue = Issues.objects.create(
    #         project=project,
    #         title=validated_data['title'],
    #         description=validated_data['description'],
    #         tag=validated_data['tag'],
    #         priority=validated_data['priority'],
    #         status=validated_data['status'],
    #         assignee_user=validated_data['assignee_user'],
    #         author_user=self._user()
    #     )
    #     issue.save()
    #     return issue


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        read_only__fields = ('author', 'issue', 'created_time', 'id')

    # def _user(self):
    #     request = self.context.get("request", None)
    #     if request:
    #         return request.user
        
    # def create(self, validated_data):
    #     issue = Issues.objects.get(id=self.context['view'].kwargs['project_pk'])
    #     comment = Comments.objects.create(
    #         issue=issue,
    #         description=validated_data['description'],
    #         author_user=self._user()
    #     )
    #     comment.save()
    #     return comment    