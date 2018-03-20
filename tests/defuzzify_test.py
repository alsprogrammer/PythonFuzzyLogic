from unittest import TestCase
from fuzzpy.defuzzification import step_generator, prec_generator


class TestStep_generator(TestCase):
    def test_step_generator_nosteps_exception(self):
        sum = 0
        with self.assertRaises(ValueError) as context:
            for x in step_generator(0, 0, 1):
                sum += 1

        self.assertTrue(isinstance(context.exception, ValueError))

    def test_step_generator_nosteps_exception(self):
        sum = 0
        with self.assertRaises(ValueError) as context:
            for x in step_generator(0, 1, 0):
                sum += 1

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


class TestPrec_generator(TestCase):
    def test_prec_generator_nosteps_exception(self):
        sum = 0
        with self.assertRaises(ValueError) as context:
            for x in prec_generator(0, 0, 1):
                sum += 1

        self.assertTrue(isinstance(context.exception, ValueError))

    def test_prec_generator_nosteps_exception(self):
        sum = 0
        with self.assertRaises(ValueError) as context:
            for x in prec_generator(0, 1, 0):
                sum += 1

        self.assertTrue(isinstance(context.exception, ValueError))

    def test_prec_generator_one(self):
        sum = 0
        for x in prec_generator(0, 1, 1):
            sum += 1
        self.assertEqual(sum, 2)

    def test_prec_generator_many(self):
        sum = 0
        for x in prec_generator(0, 10, 1):
            sum += 1
        self.assertEqual(sum, 11)
