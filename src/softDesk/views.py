from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from authentication.serializers import User
from rest_framework.permissions import IsAuthenticated
from .models import Projects, Issues, Contributors, Comments
from rest_framework.exceptions import ValidationError
from .serializers import ProjectsSerializer, IssuesSerializer, CommentsSerializer, ContributorsSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAuthorContribComment, IsAuthorContribIssue,  IsAuthorContributorsView, IsAuthorProjectsView



class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [IsAuthenticated, IsAuthorProjectsView]

    def get_queryset(self):
        return Projects.objects.filter(author_user=self.request.user)
    

    def perform_create(self,serializer):
        serializer.save(author_user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    

class ContributorsViewSet(ModelViewSet):
    queryset = Contributors.objects.all()
    serializer_class = ContributorsSerializer
    permission_classes = [IsAuthenticated, IsAuthorContribComment]

    
    def get_queryset(self):
        project_id = self.kwargs['projects_pk']
        if not Projects.objects.filter(id=project_id).exists():
            raise ValidationError(f'Project {project_id} does not exist')

        contributors = Contributors.objects.filter(project=project_id)

        return contributors

    def create(self, request, **kwargs):
        project_id = self.kwargs['projects_pk']
        data = request.data
        data['project_id'] = project_id
        try:
            Contributors.objects.get(user=data['user'], project=data)
            return Response("User has already been added", status=status.HTTP_400_BAD_REQUEST)
        except Contributors.DoesNotExist:
            try:
                User.objects.get(id=data['user'])
                serializer = self.get_serializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response("This User does not exist.", status=status.HTTP_400_BAD_REQUEST)

    # def perform_create(self, serializer):
    #     return super().perform_create(serializer)


    

class IssuesViewSet(ModelViewSet):
    queryset = Issues.objects.all()
    serializer_class = IssuesSerializer
    permission_classes = [IsAuthenticated, IsAuthorContribIssue]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')

        if not Projects.objects.filter(id=project_id).exists():
            raise ValidationError(f'Project {project_id} does not exist')

        if not Contributors.objects.filter(project_id=project_id, user_id=self.request.user).exists():
            raise ValidationError(f'Requesting user {self.request.user.username} is not a contributor of the project')

        queryset = Issues.objects.filter(project=project_id)
        return queryset

    

class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated, IsAuthorContribComment]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')

        if not Projects.objects.filter(id=project_id).exists():
            raise ValidationError(f'Project {project_id} does not exist')

        issue_id = self.kwargs.get("issues_pk")
        if not Issues.objects.filter(id=issue_id).exists():
            raise ValidationError(f'Issue_id {issue_id} does not exist')

        if not Contributors.objects.filter(project_id=project_id, id=self.request.user.id).exists():
            raise ValidationError(f'Requesting user {self.request.user.id} is not a contributor of the project')

        queryset = Comments.objects.filter(issue=issue_id)
        return queryset