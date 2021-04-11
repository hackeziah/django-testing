from django.test import TestCase, Client
from django.urls import reverse
from budget.models import Project, Category, Expense
import json


class TestModel(TestCase):

    def setUp(self):
        self.project1 = Project.objects.create(
            name='Project 1',
            budget=1000
        )

    def test_project_is_assign_slug_on_creation(self):
        self.assertEquals(self.project1.slug, 'project-1')

    def test_budget_left(self):
        category1 = Category.objects.create(
            project=self.project1,
            name='development'
        )

        Expense.objects.create(
            project=self.project1,
            title='expense1',
            amount=1000,
            category=category1
        )

        Expense.objects.create(
            project=self.project1,
            title='expense2',
            amount=6000,
            category=category1
        )

        self.assertEquals(self.project1.budget_left, -6000)

    def test_project_total_transaction(self):
        projec2 = Project.objects.create(
            name='Project 2',
            budget=10000
        )

        category1 = Category.objects.create(
            project=projec2,
            name='development'
        )

        Expense.objects.create(  # 1
            project=projec2,
            title='expense1',
            amount=1000,
            category=category1
        )

        Expense.objects.create(  # 2
            project=projec2,
            title='expense2',
            amount=2000,
            category=category1
        )

        self.assertEquals(projec2.total_transactions, 2)
