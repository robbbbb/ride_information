from rest_framework import routers
from .api.user import UserViewSet


router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = router.urls
