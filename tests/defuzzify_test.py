from unittest import TestCase

from fuzzypy import TriFunc
from fuzzypy.defuzzification import step_generator, defuzzify
from fuzzypy.variables import FuzzyRule, FuzzyVariable, build_resulting_fuzzy_term


class TestStepGenerator(TestCase):
    def test_step_gen_nosteps_exception(self):
        sum = 0
        with self.assertRaises(ValueError) as context:
            step_generator(0, 0, 1).__next__()

        self.assertTrue(isinstance(context.exception, ValueError))

    def test_step_generator_start_stop_exception(self):
        sum = 0
        with self.assertRaises(ValueError) as context:
            step_generator(0, 1, 0).__next__()

        self.assertTrue(isinstance(context.exception, ValueError))

    def test_step_generator_nosteps_exception(self):
        sum = 0
        with self.assertRaises(ValueError) as context:
            step_generator(0, 1, 0).__next__()

        self.assertTrue(isinstance(context.exception, ValueError))

    def test_step_generator_one(self):
        sum = 0
        for x in step_generator(0, 1, 1):
            sum += 1
        self.assertEqual(sum, 2)

    def test_step_generator_many(self):
        sum = 0
        for x in step_generator(0, 10, 10):
            sum += 1
        self.assertEqual(sum, 11)

    def test_step_generator_many1(self):
        sum = 0
        for x in step_generator(-1, 1, 10):
            sum += 1
        self.assertEqual(sum, 11)


class TestCOG(TestCase):
    def test_COG_one_out(self):
        in_fuzz_var = FuzzyVariable()
        in_fuzz_memb = TriFunc(-1, 0, 1)
        in_fuzz_term = in_fuzz_var.is_(in_fuzz_memb)
        out_fuzz_var = FuzzyVariable()
        out_fuzz_memb = TriFunc(-1, 0, 1)
        fuzz_rule = FuzzyRule(in_fuzz_term, out_fuzz_var, out_fuzz_memb)
        in_fuzz_var.value = 0
        fuzzy_res = build_resulting_fuzzy_term(fuzz_rule, out_fuzz_var)
        res = defuzzify(fuzzy_res)  # the default method is center-of-gravity
        self.assertAlmostEqual(res, 0, delta=0.01)
        self.assertAlmostEqual(fuzzy_res.variable.value, 0, delta=0.01)

    def test_COG_or_out(self):
        in_fuzz_var = FuzzyVariable()
        in_fuzz_memb = TriFunc(-1, 0, 1)
        in_fuzz_term = in_fuzz_var.is_(in_fuzz_memb)
        out_fuzz_var = FuzzyVariable()
        out_fuzz_memb1 = TriFunc(-2, -1, 0)
        out_fuzz_memb2 = TriFunc(0, 1, 2)
        fuzz_rule = FuzzyRule(in_fuzz_term, out_fuzz_var, out_fuzz_memb1 | out_fuzz_memb2)
        in_fuzz_var.value = 0
        fuzzy_res = build_resulting_fuzzy_term(fuzz_rule, out_fuzz_var)
        res = defuzzify(fuzzy_res)  # the default method is center-of-gravity
        self.assertAlmostEqual(res, 0, delta=0.01)

    def test_COG_two_rules_one_var(self):
        in_fuzz_var = FuzzyVariable()
        in_fuzz_memb1 = TriFunc(-1, 0, 1)
        in_fuzz_memb2 = TriFunc(-1, 0, 1)
        in_fuzz_term1 = in_fuzz_var.is_(in_fuzz_memb1)
        in_fuzz_term2 = in_fuzz_var.is_(in_fuzz_memb2)
        out_fuzz_var = FuzzyVariable()
        out_fuzz_memb1 = TriFunc(-1, 0, 1)
        out_fuzz_memb2 = TriFunc(-1, 0, 1)
        fuzz_rule1 = FuzzyRule(in_fuzz_term1, out_fuzz_var, out_fuzz_memb1)
        fuzz_rule2 = FuzzyRule(in_fuzz_term2, out_fuzz_var, out_fuzz_memb2)
        in_fuzz_var.value = 0
        fuzzy_res = build_resulting_fuzzy_term([fuzz_rule1, fuzz_rule2], out_fuzz_var)
        res = defuzzify(fuzzy_res)  # the default method is center-of-gravity
        self.assertAlmostEqual(res, 0, delta=0.01)
