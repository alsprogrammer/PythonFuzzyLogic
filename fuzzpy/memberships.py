from abc import ABC


class MembershipFunction(ABC):
    """
    Abstract class for creating of Membership function.
    The functions can be multiplied, also "and" and "or" operators are applicable
    """
    def __and__(self, other):
        def ret_func(*d, **mp):
            a = float(self(*d, **mp))
            b = float(other(*d, **mp))
            return a if a < b else b
        return ret_func

    def __or__(self, other):
        def ret_func(*d, **mp):
            a = float(self(*d, **mp))
            b = float(other(*d, **mp))
            return a if a > b else b
        return ret_func

    def __mul__(self, other):
        def ret_func(*d, **mp):
            a = float(self(*d, **mp))
            b = float(other(*d, **mp))
            return a * b
        return ret_func

    def __call__(self, x):
        return self.func(x)


class TriFunc(MembershipFunction):
    """
    The triangle membership function.
    """
    def __init__(self, x1, x2, x3):
        def trifunc(x):
            if x <= x1:
                ret = 0.0
            elif x <= x2:
                ret = (x - x1) / (x2 - x1)
            elif x <= x3:
                ret = 1 - (x - x2) / (x3 - x2)
            else:
                ret = 0.0
            return ret

        self.func = trifunc


class TrapecFunc(MembershipFunction):
    """
    The triangle membership function.
    """
    def __init__(self, x1, x2, x3, x4):
        def trapfunc(x):
            if x < x1:
                ret = 0.0
            elif x <= x2:
                ret = (x - x1) / (x2 - x1)
            elif x <= x3:
                ret = 1
            elif x <= x4:
                ret = 1 - (x - x3) / (x4 - x3)
            else:
                ret = 0.0
            return ret

        self.func = trapfunc


if __name__ == "__main__":
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
        print("x={x}, f1={f1}, f2={f2}, composition={c}".format(x=x, f1=f1, f2=f2, c=f))
