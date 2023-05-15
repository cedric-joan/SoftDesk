from rest_framework import routers
from .views import ProjectsViewSet, CommentsViewSet, ContributorsViewSet, IssuesViewSet

router = routers.DefaultRouter()
router.register('projects', ProjectsViewSet)
router.register('comments', CommentsViewSet)
router.register('contributors', ContributorsViewSet)
router.register('issues', IssuesViewSet)