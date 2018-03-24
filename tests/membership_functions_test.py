import unittest
from fuzzpy.memberships import TriFunc, TrapecFunc


class MembershipFunctionsTestCase(unittest.TestCase):
    """
    The test of the creation of triangle membership function.
    """
    def test_normal_trifunc(self):
        step = 5
        limits = [(-10, 0, 10), (-20, -10, 0), (0, 10, 20)]
        for left, center, right in limits:
            func = TriFunc(left / 10.0, center / 10.0, right / 10.0)
            for x in range(left - step, right + step, step):
                x1 = x / 10.0
                if x <= left:
                    self.assertEqual(func(x1), 0)
                elif x < center:
                    self.assertEqual(func(x1), 0.5)
                elif x == center:
                    self.assertEqual(func(x1), 1)
                elif x < right:
                    self.assertEqual(func(x1), 0.5)
                else:
                    self.assertEqual(func(x1), 0)

    def test_normal_trapecfunc(self):
        step = 5
        limits = [(-40, -30, -20, -10), (-30, -20, -10, -0), (-20, -10, 0, 10), (0, 10, 20, 30)]

        for left, left1, right1, right in limits:
            func = TrapecFunc(left / 10.0, left1 / 10.0, right1 / 10.0, right / 10.0)
            for x in range(left - step, right + 2 * step, step):
                x1 = x / 10.0
                f = func(x1)
                if x <= left:
                    self.assertEqual(f, 0)
                elif x < left1:
                    self.assertEqual(f, 0.5)
                elif x <= right1:
                    self.assertEqual(f, 1)
                elif x < right:
                    self.assertEqual(f, 0.5)
                else:
                    self.assertEqual(f, 0)

    def test_skewed_left_trifunc(self):
        left = -10
        center = 0
        right = 0
        step = 5
        func = TriFunc(left / 10.0, center / 10.0, right / 10.0)
        for x in range(left - step, right + 2 * step, step):
            x1 = x / 10.0
            if x <= left:
                self.assertEqual(func(x1), 0)
            elif x < center:
                self.assertEqual(func(x1), 0.5)
            elif x == center:
                self.assertEqual(func(x1), 1)
            else:
                self.assertEqual(func(x1), 0)

    def test_skewed_right_trifunc(self):
        left = 0
        center = 0
        right = 10
        step = 5
        func = TriFunc(left / 10.0, center / 10.0, right / 10.0)
        for x in range(left - step, right + step, step):
            x1 = x / 10.0
            if x <= left:
                self.assertEqual(func(x1), 0)
            elif x < right:
                self.assertEqual(func(x1), 0.5)
            else:
                self.assertEqual(func(x1), 0)

    def raising_trifunc_value_error(self, x1, x2, x3):
        t = TriFunc(x1, x2, x3)

    def est_trifunc_value_errors(self):
        with self.assertRaises(ValueError) as context:
            self.raising_trifunc_value_error(1, 0, 1)
        self.assertTrue(isinstance(context.exception, ValueError))

        with self.assertRaises(ValueError) as context:
            self.raising_trifunc_value_error(0, 1, 0)
        self.assertTrue(isinstance(context.exception, ValueError))

        with self.assertRaises(ValueError) as context:
            self.raising_trifunc_value_error(2, 3, 1)
        self.assertTrue(isinstance(context.exception, ValueError))

    def raising_trapfunc_value_error(self, x1, x2, x3, x4):
        t = TrapecFunc(x1=x1, x2=x2, x3=x3, x4=x4)

    def est_trapfunc_value_errors(self):
        with self.assertRaises(ValueError) as context:
            self.raising_trapfunc_value_error(1, 0, 1, 2)
        self.assertTrue(isinstance(context.exception, ValueError))

        with self.assertRaises(ValueError) as context:
            self.raising_trapfunc_value_error(2, 0, 1, 2)
        self.assertTrue(isinstance(context.exception, ValueError))

        with self.assertRaises(ValueError) as context:
            self.raising_trapfunc_value_error(0, 2, 1, 2)
        self.assertTrue(isinstance(context.exception, ValueError))

        with self.assertRaises(ValueError) as context:
            self.raising_trapfunc_value_error(0, 2, 3, 2)
        self.assertTrue(isinstance(context.exception, ValueError))

        with self.assertRaises(ValueError) as context:
            self.raising_trapfunc_value_error(0, 1, 2, 0)
        self.assertTrue(isinstance(context.exception, ValueError))


class AndOrMulMembershipFunctionsTestCase(unittest.TestCase):
    """
    The test of the application of "and" and "or" operators.
    """
    def test_and_not_intersected_trifunc(self):
        left1 = -10
        center1 = 0
        right1 = 10
        left2 = 20
        center2 = 30
        right2 = 40
        step = 5

        func1 = TriFunc(left1 / 10.0, center1 / 10.0, right1 / 10.0)
        func2 = TriFunc(left2 / 10.0, center2 / 10.0, right2 / 10.0)

        func = func2.__and__(func1)
        for x in range(left1 - step, right2 + step, step):
            x1 = x / 10.0
            f1 = func1(x1)
            f2 = func2(x1)
            f = func(x1)
            self.assertEqual(f, 0)

    def test_and_intersected_trifunc(self):
        left1 = -10
        center1 = 0
        right1 = 10
        left2 = 0
        center2 = 10
        right2 = 20
        step = 5

        func1 = TriFunc(left1 / 10.0, center1 / 10.0, right1 / 10.0)
        func2 = TriFunc(left2 / 10.0, center2 / 10.0, right2 / 10.0)

        func = func1 & func2
        for x in range(left1 - step, right2 + step, step):
            x1 = x / 10.0
            f1 = func1(x1)
            f2 = func2(x1)
            f = func(x1)
            self.assertEqual(f, min(f1, f2))

    def test_or_intersected_trifunc(self):
        left1 = -10
        center1 = 0
        right1 = 10
        left2 = 0
        center2 = 10
        right2 = 20
        step = 5

        func1 = TriFunc(left1 / 10.0, center1 / 10.0, right1 / 10.0)
        func2 = TriFunc(left2 / 10.0, center2 / 10.0, right2 / 10.0)

        func = func1 | func2
        for x in range(left1 - step, right2 + step, step):
            x1 = x / 10.0
            f1 = func1(x1)
            f2 = func2(x1)
            f = func(x1)
            self.assertEqual(f, max(f1, f2))

    def test_or_not_intersected_trifunc(self):
        left1 = -10
        center1 = 0
        right1 = 10
        left2 = 10
        center2 = 20
        right2 = 30
        step = 5

        func1 = TriFunc(left1 / 10.0, center1 / 10.0, right1 / 10.0)
        func2 = TriFunc(left2 / 10.0, center2 / 10.0, right2 / 10.0)

        func = func1 | func2
        for x in range(left1 - step, right2 + step, step):
            x1 = x / 10.0
            f1 = func1(x1)
            f2 = func2(x1)
            f = func(x1)
            self.assertEqual(f, max(f1, f2))

    def test_mul_intersected_trifunc(self):
        left1 = -10
        center1 = 0
        right1 = 10
        left2 = 0
        center2 = 10
        right2 = 20
        step = 5

        func1 = TriFunc(left1 / 10.0, center1 / 10.0, right1 / 10.0)
        func2 = TriFunc(left2 / 10.0, center2 / 10.0, right2 / 10.0)

        func = func1 * func2
        for x in range(left1 - step, right2 + step, step):
            x1 = x / 10.0
            f1 = func1(x1)
            f2 = func2(x1)
            f = func(x1)
            self.assertEqual(f, f1 * f2)
