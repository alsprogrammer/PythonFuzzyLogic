from abc import ABC


class MembershipFunction(ABC):
    """
    Abstract class for creating of Membership function.
    The functions can be multiplied, also "and" and "or" operators are applicable
    """
    def __and__(self, other):
        def ret_func(*d, **mp):
            return min(float(self(*d, **mp)), float(other(*d, **mp)))
        return ret_func

    def __or__(self, other):
        def ret_func(*d, **mp):
            return max(float(self(*d, **mp)), float(other(*d, **mp)))
        return ret_func

    def __mul__(self, other):
        def ret_func(*d, **mp):
            return float(self(*d, **mp)) * float(other(*d, **mp))
        return ret_func

    def __call__(self, x):
        return self.func(x)


class TriFunc(MembershipFunction):
    """
    The triangle membership function.
    """
    def __init__(self, x1, x2, x3):
        if x1 < x2 and x2 < x3:
            self.__points = [x1, x2, x3]
            self.left_border = min(self.__points)
            self.right_border = max(self.__points)

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
        else:
            raise ValueError("x1 < x2 < x3")


class TrapecFunc(MembershipFunction):
    """
    The triangle membership function.
    """
    def __init__(self, x1, x2, x3, x4):
        if x1 < x2 and x2 < x3 and x3 < x4:
            self.__points = [x1, x2, x3, x4]
            self.left_border = min(self.__points)
            self.right_border = max(self.__points)

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
        else:
            raise ValueError("x1 < x2 < x3 < x4")
