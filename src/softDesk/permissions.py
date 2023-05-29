from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.shortcuts import get_object_or_404
from .models import Contributors, Projects

MESSAGE_ERROR = "accès refusé !"

class IsAuthorProjectsView(BasePermission):

    def has_permission(self, request, project_id):
        project = get_object_or_404(Projects, pk=project_id)
        contributor = Contributors.objects.filter(project=project, user=request.user)
        if project.author_user_id == request.user:
            return True
        if contributor.role == 'A':
            return True
        return MESSAGE_ERROR

class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request):
        return bool(request.user
                    and request.user.is_authenticated
                    and request.user.is_superuser)
    

class IsContributorProjectsView(BasePermission):
     
    def has_permission(self, request, project_id):
        project = get_object_or_404(Projects, pk=project_id)
        contributor = Contributors.objects.filter(project=project, user=request.user)
        if project.author_user_id == request.user:
            return True
        if contributor.role == 'C':
            return True
        return MESSAGE_ERROR
     
    # def has_object_permission(self, request, obj):
    #     if request.method in SAFE_METHODS:
    #         return True
    #     return bool(request.user == obj.author_user_id
    #                 and request.user.is_authenticated)