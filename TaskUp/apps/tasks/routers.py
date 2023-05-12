from rest_framework.routers import SimpleRouter
from .views import CommentViewSet, LabelViewSet, ProjectViewSet, TaskViewSet

router = SimpleRouter()
router.register("projects", ProjectViewSet)
router.register("tasks", TaskViewSet)
router.register("labels", LabelViewSet)
router.register("comments", CommentViewSet)
