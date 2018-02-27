import unittest
from fuzzpy.membership import TriFunc


class MembershipFunctionsTestCase(unittest.TestCase):
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

    def test_skewed_trifunc(self):
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


if __name__ == "__main__":
    unittest.main()
