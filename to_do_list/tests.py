from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from to_do_list.models import Tag, Task


class TodoListTests(TestCase):
	def test_home_orders_open_tasks_before_completed_tasks(self):
		first = Task.objects.create(content="Older open")
		newer = Task.objects.create(content="Newer open")
		completed = Task.objects.create(content="Completed", is_done=True)
		Task.objects.filter(pk=first.pk).update(created_at=timezone.now() - timedelta(days=1))
		Task.objects.filter(pk=newer.pk).update(created_at=timezone.now())

		response = self.client.get(reverse("to_do_list:home"))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(list(response.context["tasks"]), [newer, first, completed])

	def test_task_can_be_completed_and_undone(self):
		task = Task.objects.create(content="Write tests")
		toggle_url = reverse("to_do_list:task-toggle", args=[task.pk])

		response = self.client.post(toggle_url)
		task.refresh_from_db()
		self.assertRedirects(response, reverse("to_do_list:home"))
		self.assertTrue(task.is_done)

		self.client.post(toggle_url)
		task.refresh_from_db()
		self.assertFalse(task.is_done)

	def test_task_form_saves_multiple_tags_and_deadline(self):
		tags = [Tag.objects.create(name=name) for name in ["Work", "Home"]]

		response = self.client.post(
			reverse("to_do_list:task-create"),
			{
				"content": "Plan week",
				"deadline": "2026-10-05T12:30",
				"tags": [tag.pk for tag in tags],
			},
		)

		self.assertRedirects(response, reverse("to_do_list:home"))
		task = Task.objects.get(content="Plan week")
		self.assertEqual(set(task.tags.all()), set(tags))
		self.assertIsNotNone(task.deadline)

	def test_tag_page_and_update_route(self):
		tag = Tag.objects.create(name="Personal")

		response = self.client.get(reverse("to_do_list:tags"))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Personal")
		update_response = self.client.post(
			reverse("to_do_list:tag-update", args=[tag.pk]), {"name": "Study"}
		)
		self.assertRedirects(update_response, reverse("to_do_list:tags"))
		tag.refresh_from_db()
		self.assertEqual(tag.name, "Study")
