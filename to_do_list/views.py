from django.shortcuts import get_object_or_404, redirect, render

from to_do_list.forms import TagForm, TaskForm
from to_do_list.models import Tag, Task


def task_list(request):
	tasks = Task.objects.prefetch_related("tags").order_by("is_done", "-created_at")
	return render(request, "to_do_list/task_list.html", {"tasks": tasks})


def task_create(request):
	form = TaskForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		form.save()
		return redirect("to_do_list:home")
	return render(request, "to_do_list/form.html", {"form": form, "title": "Add task"})


def task_update(request, pk):
	task = get_object_or_404(Task, pk=pk)
	form = TaskForm(request.POST or None, instance=task)
	if request.method == "POST" and form.is_valid():
		form.save()
		return redirect("to_do_list:home")
	return render(
		request,
		"to_do_list/form.html",
		{"form": form, "title": "Update task", "object": task},
	)


def task_delete(request, pk):
	task = get_object_or_404(Task, pk=pk)
	if request.method == "POST":
		task.delete()
		return redirect("to_do_list:home")
	return render(
		request,
		"to_do_list/confirm_delete.html",
		{"object": task, "title": "Delete task", "cancel_url": "to_do_list:home"},
	)


def task_toggle(request, pk):
	task = get_object_or_404(Task, pk=pk)
	if request.method == "POST":
		task.is_done = not task.is_done
		task.save(update_fields=["is_done"])
	return redirect("to_do_list:home")


def tag_list(request):
	tags = Tag.objects.all()
	return render(request, "to_do_list/tag_list.html", {"tags": tags})


def tag_create(request):
	form = TagForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		form.save()
		return redirect("to_do_list:tags")
	return render(request, "to_do_list/form.html", {"form": form, "title": "Add tag"})


def tag_update(request, pk):
	tag = get_object_or_404(Tag, pk=pk)
	form = TagForm(request.POST or None, instance=tag)
	if request.method == "POST" and form.is_valid():
		form.save()
		return redirect("to_do_list:tags")
	return render(
		request,
		"to_do_list/form.html",
		{"form": form, "title": "Update tag", "object": tag},
	)


def tag_delete(request, pk):
	tag = get_object_or_404(Tag, pk=pk)
	if request.method == "POST":
		tag.delete()
		return redirect("to_do_list:tags")
	return render(
		request,
		"to_do_list/confirm_delete.html",
		{"object": tag, "title": "Delete tag", "cancel_url": "to_do_list:tags"},
	)
