import unittest
from fuzzypy.variables import FuzzyVariable, FuzzyTerm, FuzzyRule
from fuzzypy.memberships import TriFunc


class FuzzTermTest(unittest.TestCase):
    """
    The test of fuzzy term
    """
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


class FuzzyVar(unittest.TestCase):
    """
    The test of fuzzy var
    """
    def test_term_generation(self):
        limits1 = (-2, -1, 0)
        limits2 = (0, 1, 2)
        fuzzy_var = FuzzyVariable()
        trifunc1 = TriFunc(limits1[0], limits1[1], limits1[2])
        trifunc2 = TriFunc(limits2[0], limits2[1], limits2[2])
        fuzzy_var.is_(trifunc1)
        self.assertEqual(fuzzy_var.low_limit, limits1[0])
        self.assertEqual(fuzzy_var.upp_limit, limits1[2])
        fuzzy_var.is_(trifunc2)
        self.assertEqual(fuzzy_var.low_limit, min(limits1[0], limits2[0]))
        self.assertEqual(fuzzy_var.upp_limit, max(limits1[2], limits2[2]))


class TestFuzzyRule(unittest.TestCase):
    def test_rule_creation_one_anrecedent(self):
        input_fuzzy_var = FuzzyVariable()
        input_membership_func = TriFunc(-1, 0, 1)
        input_fuzzy_term = input_fuzzy_var.is_(input_membership_func)
        output_fuzzy_var = FuzzyVariable()
        output_membership_func = TriFunc(100, 200, 300)
        fuzzy_rule = FuzzyRule(input_fuzzy_term, output_fuzzy_var, output_membership_func)
        self.assertEqual(len(fuzzy_rule.antecedents), 1)
        self.assertEqual(fuzzy_rule.variable.low_limit, 100)
        self.assertEqual(fuzzy_rule.variable.upp_limit, 300)

    def test_rule_creation_two_anrecedents(self):
        input_fuzzy_var = FuzzyVariable()
        input_membership_func1 = TriFunc(-1, 0, 1)
        input_membership_func2 = TriFunc(1, 2, 3)
        input_fuzzy_term1 = input_fuzzy_var.is_(input_membership_func1)
        input_fuzzy_term2 = input_fuzzy_var.is_(input_membership_func2)
        output_fuzzy_var = FuzzyVariable()
        output_membership_func = TriFunc(100, 200, 300)
        fuzzy_rule = FuzzyRule([input_fuzzy_term1, input_fuzzy_term2], output_fuzzy_var, output_membership_func)
        self.assertEqual(len(fuzzy_rule.antecedents), 2)

    def test_rule_call(self):
        input_fuzzy_var = FuzzyVariable()
        input_membership_func = TriFunc(-1, 0, 1)
        input_fuzzy_term = input_fuzzy_var.is_(input_membership_func)
        output_fuzzy_var = FuzzyVariable()
        output_membership_func = TriFunc(100, 200, 300)
        fuzzy_rule = FuzzyRule(input_fuzzy_term, output_fuzzy_var, output_membership_func)

        input_fuzzy_var.value = 0
        self.assertEqual(fuzzy_rule(200), 1)
        self.assertEqual(fuzzy_rule(100), 0)
        self.assertEqual(fuzzy_rule(150), 0.5)
        self.assertEqual(fuzzy_rule(250), 0.5)
        self.assertEqual(fuzzy_rule(300), 0)

        input_fuzzy_var.value = -1
        self.assertEqual(fuzzy_rule(200), 0)
        self.assertEqual(fuzzy_rule(100), 0)
        self.assertEqual(fuzzy_rule(150), 0)
        self.assertEqual(fuzzy_rule(250), 0)
        self.assertEqual(fuzzy_rule(300), 0)

        input_fuzzy_var.value = 1
        self.assertEqual(fuzzy_rule(200), 0)
        self.assertEqual(fuzzy_rule(100), 0)
        self.assertEqual(fuzzy_rule(150), 0)
        self.assertEqual(fuzzy_rule(250), 0)
        self.assertEqual(fuzzy_rule(300), 0)

        input_fuzzy_var.value = 0.5
        self.assertEqual(fuzzy_rule(200), 0.5)
        self.assertEqual(fuzzy_rule(100), 0)
        self.assertEqual(fuzzy_rule(150), 0.25)
        self.assertEqual(fuzzy_rule(250), 0.25)
        self.assertEqual(fuzzy_rule(300), 0)


