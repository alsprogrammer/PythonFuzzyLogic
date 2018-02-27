import unittest
from fuzzpy.membership import TriFunc


class MembershipFunctionsTestCase(unittest.TestCase):
    """
    The test of the creation of triangle membership function.
    """
    def SetUp(self):
        pass

    def test_normal_trifunc(self):
        left = -10
        center = 0
        right = 10
        step = 5

        func = TriFunc([left / 10.0, center / 10.0, right / 10.0])
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

    def test_skewed_left_trifunc(self):
        left = -10
        center = 0
        right = 0
        step = 5

        func = TriFunc([left / 10.0, center / 10.0, right / 10.0])
        for x in range(left - step, right + step, step):
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

        func = TriFunc([left / 10.0, center / 10.0, right / 10.0])
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


class AndOrMembershipFunctionsTestCase(unittest.TestCase):
    """
    The test of the application of "and" and "or" operators.
    """
    def SetUp(self):
        pass

    def test_and_not_intersected_trifunc(self):
        left1 = -10
        center1 = 0
        right1 = 10
        left2 = 10
        center2 = 20
        right2 = 30
        step = 5

        func1 = TriFunc([left1 / 10.0, center1 / 10.0, right1 / 10.0])
        func2 = TriFunc([left2 / 10.0, center2 / 10.0, right2 / 10.0])

        func = func1 and func2
        for x in range(left1 - step, right2 + step, step):
            x1 = x / 10.0
            f1 = func1(x1)
            f2 = func2(x1)
            f = func(x1)
            self.assertEqual(f, 0)


if __name__ == "__main__":
    unittest.main()
