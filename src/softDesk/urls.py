from rest_framework import routers
from .views import ProjectsViewSet, CommentsViewSet, ContributorsViewSet, IssuesViewSet

router = routers.SimpleRouter()
router.register('projects', ProjectsViewSet, basename='projects')
router.register('comments', CommentsViewSet, basename='comments')
router.register('contributors', ContributorsViewSet, basename='contributors')
router.register('issues', IssuesViewSet, basename='issues')