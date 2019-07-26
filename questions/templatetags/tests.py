from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from questions import models, views, forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class QuestionTests(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(
            'john', 'john@email.com', 'Thisw0rd')

        self.author = authenticate(username='john', password='Thisw0rd')

        self.question = models.Question.objects.create(
            title="Python Testing",
            body="What is python testing",
            author = self.author
        )

    def test_question_creation(self):
        now = timezone.now()
        self.assertLess(self.question.created_at, now)

    def test_question_list_view(self):
        resp = self.client.get(reverse('questions:question_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.question, resp.context['questions'])
        self.assertTemplateUsed(resp, 'questions/question_list.html')
        self.assertContains(resp, self.question.title)

    def test_question_detail_view(self):
        resp = self.client.get(reverse('questions:question_detail', 
                                kwargs={'pk':self.question.pk}))
        self.assertContains(resp, self.question.title)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'questions/question_detail.html')

    def tearDown(self):
        self.question.delete()
        self.new_user.delete()