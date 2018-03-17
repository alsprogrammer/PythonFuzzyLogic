import unittest
from fuzzpy.variables import FuzzyVariable, FuzzyTerm, FuzzyRule
from fuzzpy.memberships import TriFunc, TrapecFunc


class FuzzTermTest(unittest.TestCase):
    def test_term_is_callable(self):
        limits = (-1, 0, 1)
        fuzzy_var = FuzzyVariable()
        trifunc = TriFunc(limits[0], limits[1], limits[2])
        fuzzy_term = fuzzy_var.is_(trifunc)
        fuzzy_var.value = limits[0]
        self.assertEqual(fuzzy_term(), 0)
        fuzzy_var.value = limits[1]
        self.assertEqual(fuzzy_term(), 1)
        fuzzy_var.value = limits[2]
        self.assertEqual(fuzzy_term(), 0)

    def test_terms_combination(self):
        limits1 = (-2, -1, 0)
        limits2 = (0, 1, 2)
        fuzzy_var = FuzzyVariable()
        trifunc1 = TriFunc(limits1[0], limits1[1], limits1[2])
        trifunc2 = TriFunc(limits2[0], limits2[1], limits2[2])
        fuzzy_term1 = fuzzy_var.is_(trifunc1)
        fuzzy_term2 = fuzzy_var.is_(trifunc2)
        fuzzy_term = fuzzy_term1 & fuzzy_term2
        self.assertTrue(isinstance(fuzzy_term, FuzzyTerm))

    def test_and_term1(self):
        limits1 = (-2, -1, 0)
        limits2 = (0, 1, 2)
        fuzzy_var = FuzzyVariable()
        trifunc1 = TriFunc(limits1[0], limits1[1], limits1[2])
        trifunc2 = TriFunc(limits2[0], limits2[1], limits2[2])
        fuzzy_term1 = fuzzy_var.is_(trifunc1)
        fuzzy_term2 = fuzzy_var.is_(trifunc2)
        fuzzy_term = fuzzy_term1 & fuzzy_term2
        for x in list(limits1) + list(limits2):
            fuzzy_var.value = x
            self.assertEqual(fuzzy_term(), 0)

    def test_and_term2(self):
        limits1 = (-1, 0, 1)
        limits2 = (0, 1, 2)
        fuzzy_var = FuzzyVariable()
        trifunc1 = TriFunc(limits1[0], limits1[1], limits1[2])
        trifunc2 = TriFunc(limits2[0], limits2[1], limits2[2])
        fuzzy_term1 = fuzzy_var.is_(trifunc1)
        fuzzy_term2 = fuzzy_var.is_(trifunc2)
        fuzzy_term = fuzzy_term1 & fuzzy_term2
        for x in list(limits1) + list(limits2):
            fuzzy_var.value = x
            self.assertEqual(fuzzy_term(), min(trifunc1(x), trifunc2(x)))

    def test_or_term1(self):
        limits1 = (-2, -1, 0)
        limits2 = (0, 1, 2)
        fuzzy_var = FuzzyVariable()
        trifunc1 = TriFunc(limits1[0], limits1[1], limits1[2])
        trifunc2 = TriFunc(limits2[0], limits2[1], limits2[2])
        fuzzy_term1 = fuzzy_var.is_(trifunc1)
        fuzzy_term2 = fuzzy_var.is_(trifunc2)
        fuzzy_term = fuzzy_term1 | fuzzy_term2
        for x in list(limits1) + list(limits2):
            fuzzy_var.value = x
            self.assertEqual(fuzzy_term(), max(trifunc1(x), trifunc2(x)))

    def test_or_term2(self):
        limits1 = (-1, 0, 1)
        limits2 = (0, 1, 2)
        fuzzy_var = FuzzyVariable()
        trifunc1 = TriFunc(limits1[0], limits1[1], limits1[2])
        trifunc2 = TriFunc(limits2[0], limits2[1], limits2[2])
        fuzzy_term1 = fuzzy_var.is_(trifunc1)
        fuzzy_term2 = fuzzy_var.is_(trifunc2)
        fuzzy_term = fuzzy_term1 | fuzzy_term2
        for x in list(limits1) + list(limits2):
            fuzzy_var.value = x
            self.assertEqual(fuzzy_term(), max(trifunc1(x), trifunc2(x)))


if __name__ == "__main__":
    unittest.main()
