import unittest
from app import roll_dice, get_fortune, is_even class TestAppFunctions(unittest.TestCase):
def test_roll_dice_range(self):
# Test if dice roll produces values strictly between 1 and 6
for _ in range(100): result = roll_dice()
self.assertTrue(1 <= result <= 6)

def test_get_fortune(self):
# Test if fortune message correctly includes the provided name
name = "Alex"
result = get_fortune(name) self.assertIn("Hello Alex", result)

def test_is_even(self):
# Test logic for even and odd numbers self.assertTrue(is_even(4)) self.assertTrue(is_even(0)) self.assertFalse(is_even(7))

if   name	 == "  main  ": unittest.main()
