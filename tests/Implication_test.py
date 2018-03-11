import unittest
from fuzzpy.implications import mamdani, larsen


class MembershipFunctionsTestCase(unittest.TestCase):
    """
    The test of the creation of triangle membership function.
    """
    def test_larsen(self):
        vals = [(0, 0), (0, 1), (1, 0), (1, 1), (0.5, 0.5)]

        for value, level in vals:
            self.assertEqual(value * level, larsen(value,level))

    def test_mamdani(self):
        vals = [(0, 0), (0, 1), (1, 0), (1, 1), (0.5, 0.5)]

        for value, level in vals:
            self.assertEqual(min(value, level), mamdani(value,level))
