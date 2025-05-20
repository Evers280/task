from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TasksViewSet, MastersViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'tasks', TasksViewSet)
router.register(r'masters', MastersViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('taskMaster/', include(router.urls)),
]