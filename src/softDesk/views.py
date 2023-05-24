from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectsSerializer, CommentsSerializer, ContributorsSerializer, IssuesSerializer 
from .models import Projects, Comments, Contributors, Issues
# from softDesk.permissions import IsAdminAuthenticated, IsStaffAuthenticated

class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    filterset_fields = ['title', 'type']
    # permission_classes = [IsAdminAuthenticated, IsStaffAuthenticated]

    # def get_queryset(self):
    #     project_author_user = Projects.objects.filter(author_user=self.request.user)
    #     return project_author_user


class ContributorsViewSet(ModelViewSet):
    serializer_class = ContributorsSerializer
    filterset_fields = ['permission', 'role']
    # permission_classes = [IsAdminAuthenticated, IsStaffAuthenticated]

    def get_queryset(self):
        queryset = Contributors.objects.all()
        project_id = self.request.GET.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(project_id=project_id)
        return queryset

class CommentsViewSet(ModelViewSet):
    serializer_class = CommentsSerializer
    filterset_fields = ['created_time']
    # permission_classes = [IsAdminAuthenticated, IsStaffAuthenticated]

    def get_queryset(self):
        queryset = Comments.objects.all()
        issue_id = self.request.GET.get('issue_id')
        if issue_id is not None:
            queryset = queryset.filter(issue_id=issue_id)
        return queryset

class IssuesViewSet(ModelViewSet):
    serializer_class = IssuesSerializer
    filterset_fields = ['priority', 'status', 'created_time']
    # permission_classes = [IsAdminAuthenticated, IsStaffAuthenticated]

    def get_queryset(self):
        queryset = Issues.objects.all()
        project_id = self.request.GET.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(project_id=project_id)
        return queryset