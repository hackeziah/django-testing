from django.test import SimpleTestCase
from budget.forms import ExpenseForm


class TestForms(SimpleTestCase):

    def text_expense_form_valid_data(self):
        form = ExpenseForm(data={
            'title': 'Expense1',
            'amount': 10000,
            'category': 'Development'
        })

        self.assertTrue(form.is_valid())

    def test_expense_from_no_data(self):
        form = ExpenseForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
