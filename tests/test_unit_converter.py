import unittest

from UnitConv import convert_length


class ConvertLengthTests(unittest.TestCase):
    def test_converts_meter_to_foot(self):
        self.assertAlmostEqual(convert_length(1, "meter", "foot"), 3.280839895)

    def test_converts_yard_to_inch(self):
        self.assertAlmostEqual(convert_length(2, "yard", "inch"), 72)

    def test_keeps_value_when_units_match(self):
        self.assertEqual(convert_length(12.5, "meter", "meter"), 12.5)

    def test_accepts_numeric_text(self):
        self.assertAlmostEqual(convert_length("12", "inch", "foot"), 1)

    def test_rejects_unknown_unit(self):
        with self.assertRaises(ValueError):
            convert_length(1, "kilometer", "meter")


if __name__ == "__main__":
    unittest.main()
