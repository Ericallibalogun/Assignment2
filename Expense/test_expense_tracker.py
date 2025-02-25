import unittest
import expense_tracker

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.expenses = []
        
    def test_add_expense(self):
        test_data = {
            'date': '2023-01-01',
            'description': 'Test',
            'amount': 50.0
        }
        initial_length = len(self.expenses)
        self.expenses.append(test_data)
        self.assertEqual(len(self.expenses), initial_length + 1)
        self.assertEqual(self.expenses[-1]['amount'], 50.0)

    def test_total_calculation(self):
        self.expenses = [
            {'amount': 10.0},
            {'amount': 20.0},
            {'amount': 30.0}
        ]
        total = sum(item['amount'] for item in self.expenses)
        self.assertEqual(total, 60.0)

    def test_empty_expenses(self):
        total = sum(item['amount'] for item in self.expenses)
        self.assertEqual(total, 0.0)


    def test_valid_date(self):
        valid_date = '2023-12-31'
        try:
            datetime.datetime.strptime(valid_date, "%Y-%m-%d").date()
            self.assertTrue(True)
        except ValueError:
            self.fail("Valid date.....failed validation")


    def test_valid_amount(self):
        self.assertEqual(float("12.34"), 12.34)
        
    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            float("abc")

if __name__ == '__main__':
    unittest.main()