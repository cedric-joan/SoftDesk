from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.shortcuts import get_object_or_404

from .models import Comments, Contributors, Issues, Projects

"""CUSTOM PERMISSIONS"""


class IsAuthorProjectsView(BasePermission):
    """
    Check if user is author or contributor for project
    http_methods : destroy, update
    """
    def has_permission(self, request, view):
        if view.action in ("destroy", "update"):
            try:
                project = Projects.objects.get(pk=view.kwargs["pk"])
            except ObjectDoesNotExist:
                return False
            return project.author_user == request.user
        return True


class IsAdminContributors(BasePermission):
    """ Custom permission to only allow the author of the project to add or
    delete contributors in the project. """

    message = "You are not the author of the project."

    def has_permission(self, request, view):
        project_id = request.resolver_match.kwargs['projects_pk']
        project = get_object_or_404(Projects, pk=project_id)
        if request.method in SAFE_METHODS:
            return True
        elif project.author_user == request.user:
            return True
        return False
        

class IsContributorView(BasePermission):
    """
    Check if user is author or contributor for a issue
    http_methods : list, retrieve, create
    """

    def has_permission(self, request,view):
        project_id = request.resolver_match.kwargs['projects_pk']
        project = get_object_or_404(Projects, pk=project_id)
        contributor = Contributors.objects.filter(user_id=request.user.id)
        if request.method in SAFE_METHODS:
            return True
        elif project.author_user == request.user or bool(contributor):
            return True
        return False
    

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author_user == request.user


# class IsContributorComment(BasePermission):
#     """
#     Check if user is author or contributor for a comment
#     http_methods : list, retrieve, create
#     """

#     def has_permission(self, request, view):
#         if view.action in ("list", "retrieve", "create"):
#             try:
#                 project = Projects.objects.get(id=view.kwargs["pk"])
#             except ObjectDoesNotExist:
#                 return False
#             is_contributor_comment = Contributors.objects.filter(
#                 project_id=view.kwargs["projects_pk"]
#             ).filter(user=request.user.id)

#             if project.author_user == request.user or bool(is_contributor_comment):
#                 return True

#         if view.action in ("destroy", "update"):
#             try:
#                 comment = Comments.objects.get(id=view.kwargs["pk"])
#             except ObjectDoesNotExist:
#                 return False
#             return comment.author_user == request.user
#         return False