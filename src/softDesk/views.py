from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectsSerializer, CommentsSerializer, ContributorsSerializer, IssuesSerializer 
from .models import Projects, Comments, Contributors, Issues

class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    filterset_fields = ['title', 'type']

class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    filterset_fields = ['created_time']

class ContributorsViewSet(ModelViewSet):
    queryset = Contributors.objects.all()
    serializer_class = ContributorsSerializer
    filterset_fields = ['permission', 'role']

class IssuesViewSet(ModelViewSet):
    queryset = Issues.objects.all()
    serializer_class = IssuesSerializer
    filterset_fields = ['priority', 'status', 'created_time']