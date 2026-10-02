from django.urls import path

from . import views

app_name = "to_do_list"

urlpatterns = [
    path("", views.task_list, name="home"),
    path("tasks/add/", views.task_create, name="task-create"),
    path("tasks/<int:pk>/edit/", views.task_update, name="task-update"),
    path("tasks/<int:pk>/delete/", views.task_delete, name="task-delete"),
    path("tasks/<int:pk>/toggle/", views.task_toggle, name="task-toggle"),
    path("tags/", views.tag_list, name="tags"),
    path("tags/add/", views.tag_create, name="tag-create"),
    path("tags/<int:pk>/edit/", views.tag_update, name="tag-update"),
    path("tags/<int:pk>/delete/", views.tag_delete, name="tag-delete"),
]