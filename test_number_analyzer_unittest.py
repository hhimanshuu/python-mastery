import unittest
from number_analyzer import analyze_numbers

class TestAnalyzeNumbers(unittest.TestCase):

    def test_total(self):
        result = analyze_numbers([10, 20, 30])
        self.assertEqual(result["total"], 60)

    def test_empty_list(self):
        result = analyze_numbers([])
        self.assertEqual(result["average"], 0)

    def test_largest_even(self):
        result = analyze_numbers([10, 20, 30])
        self.assertEqual(result["largest_even"], 30)

    def test_no_even_numbers(self):
        result = analyze_numbers([1, 3, 5])
        self.assertIsNone(result["largest_even"])    

    def test_above_threshold(self):
        result = analyze_numbers([10, 20, 30, 40], threshold=30)
        self.assertEqual(result["above_threshold"], [40])    

    def test_above_and_equal(self):
        result = analyze_numbers([10, 20, 30, 40], threshold=30, include_equal=True)
        self.assertEqual(result["above_threshold"], [30,40])

    def test_default_threshold(self):
        result = analyze_numbers([1, 2, 3])
        self.assertEqual(result["above_threshold"], [1, 2, 3])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            result = analyze_numbers("hello")

    def test_invalid_item(self):
        with self.assertRaises(TypeError):
            analyze_numbers([54, "Hello", 56])

if __name__ == "__main__":
    unittest.main()