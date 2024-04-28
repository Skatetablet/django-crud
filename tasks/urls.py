from django.urls import path, include
from rest_framework import routers
from tasks import views

router = routers.DefaultRouter()
router.register(r"task", views.TaskView, "tasks")
urlpatterns = [
    path("api/tasks/", include(router.urls))

]