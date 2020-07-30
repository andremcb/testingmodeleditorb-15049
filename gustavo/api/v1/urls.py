from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import GordinhoViewSet

router = DefaultRouter()
router.register("gordinho", GordinhoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
