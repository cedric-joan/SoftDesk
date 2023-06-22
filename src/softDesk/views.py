from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
# from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from authentication.serializers import User
from rest_framework.permissions import IsAuthenticated
from .models import Projects, Issues, Contributors, Comments
from rest_framework.exceptions import ValidationError
from .serializers import ProjectsSerializer, IssuesSerializer, CommentsSerializer, ContributorsSerializer
from .permissions import IsContributorView, IsAuthorProjectsView, IsAdminContributors


class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [IsAuthenticated, IsAuthorProjectsView]

    def get_queryset(self):
        return Projects.objects.filter(author_user=self.request.user)
    

    def perform_create(self,serializer):
        serializer.save(author_user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class ContributorsViewSet(ModelViewSet):
    queryset = Contributors.objects.all()
    serializer_class = ContributorsSerializer
    permission_classes = [IsAuthenticated, IsAdminContributors]

    
    def get_queryset(self):
        project_id = self.kwargs['projects_pk']
        if not Projects.objects.filter(id=project_id).exists():
            raise ValidationError(f'Project {project_id} does not exist')
        contributors = Contributors.objects.filter(project=project_id)
        return contributors

    def perform_create(self, serializer):
        project_id = self.kwargs.get('projects_pk')
        if not Projects.objects.filter(id=project_id).exists():
            raise ValidationError(f'Project {project_id} does not exist')
        author = Projects.objects.filter(id=project_id, author_user=self.request.user)
        if not author:
            raise ValidationError(f'Requesting user {self.request.user.username} is not the project author')
        if int(project_id) != int(serializer.data['project']):
            raise ValidationError(f'project_id in URL {project_id} should equal to the form parameter')
        if serializer.data['permission'] != 'CR':
            raise ValidationError('permission should be CR')
        if serializer.data['role'] != 'C':
            raise ValidationError('role should be C')
        user = User.objects.get(id=serializer.data['user'])
        if serializer.data['user'] != user.pk:
            raise ValidationError('User has not been added')
        serializer = ContributorsSerializer(data=serializer.data)
        if serializer.is_valid(raise_exception=True):
            Contributors.objects.create(user=user, project_id=project_id, role='C', permission='CR')
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
class IssuesViewSet(ModelViewSet):
    queryset = Issues.objects.all()
    serializer_class = IssuesSerializer
    permission_classes = [IsAuthenticated, IsContributorView]

    def get_queryset(self):
        project_id = self.kwargs['projects_pk']
        if not Projects.objects.filter(id=project_id).exists():
            raise ValidationError(f'Project {project_id} does not exist')
        issues = Issues.objects.filter(project=project_id)
        return issues


    def perform_create(self, serializer):
        project_id = self.kwargs.get('projects_pk')
        if not Projects.objects.filter(id=project_id).exists():
            raise ValidationError(f'Project {project_id} does not exist')
        # author = Projects.objects.filter(id=project_id, author_user=self.request.user)
        # if not author:
        #     raise ValidationError(f'Requesting user {self.request.user.username} is not the project author')
        if int(project_id) != int(serializer.data['project']):
            raise ValidationError(f'project_id {project_id} is different in the URL and in the form')
        if Contributors.objects.filter(project_id=project_id, user_id=self.request.user).exists():
            return True
        issue_data = self.request.data
        user = User.objects.get(id=issue_data['author_user'])
        if int(self.request.user.id) != int(user.id):
            raise ValidationError('Requesting user should equal to author_user')
        contributor_id = issue_data['assignee_user']
        if not Contributors.objects.filter(project=project_id, id=contributor_id).exists():
            raise ValidationError(f'Assignee_user {contributor_id} is not a contributor of the project')
        assignee_user_id = Contributors.objects.get(id=contributor_id)
        serializer = ProjectsSerializer(data=issue_data)
        if serializer.is_valid(raise_exception=True):
            Issues.objects.create(title=issue_data['title'], description=issue_data['description'],
                                    tag=issue_data['tag'], project_id=project_id, 
                                    priority=issue_data['priority'], status=issue_data['status'], 
                                    author_user=user, assignee_user=assignee_user_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated, IsContributorView]

    def get_queryset(self):
        project_id = self.kwargs.get('projects_pk')

        if not Projects.objects.filter(id=project_id).exists():
            raise ValidationError(f'Project {project_id} does not exist')
        issue_id = self.kwargs.get("issues_pk")
        if not Issues.objects.filter(id=issue_id).exists():
            raise ValidationError(f'Issue_id {issue_id} does not exist')
        queryset = Comments.objects.filter(issue=issue_id)
        return queryset
    
    def perform_create(self, serializer):
        # project_id = self.kwargs.get('projects_pk')
        # if not Projects.objects.filter(project=project_id).exists():
        #     raise ValidationError(f'Project {project_id} does not exist')
        issue_id = self.kwargs.get('issues_pk')
        if not Issues.objects.filter(id=issue_id).exists():
            raise ValidationError(f'Issue {issue_id} does not exist')
        # if not Contributors.objects.filter(project=project_id, user_id=self.request.user.id).exists():
        #     raise ValidationError(f'Requesting user {self.request.user.id} is not a contributor of the project')
        comment_data = self.request.data
        user = User.objects.get(id=comment_data['author_user'])
        serializer = CommentsSerializer(data=comment_data)
        if serializer.is_valid():
            Comments.objects.create(description=comment_data['description'], 
                                    author_user=user, 
                                    issue_id=comment_data['issue'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_update(self, serializer):
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)        