import unittest
impot calculator

class Tests(unittest.TestCase):
  def test_add(self):
    self.assertEqual(calculator.add(2, 3), 5)
