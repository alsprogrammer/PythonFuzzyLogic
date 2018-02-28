from abc import ABC


class MembershipFunction(ABC):
    """
    Abstract class for creating of Membership function.
    The functions can be multiplied, also "and" and "or" operators are applicable
    """
    def __and__(self, other):
        ret_func = lambda *dt, **mp: min([self(*dt, **mp), other(*dt, **mp)])
        return ret_func

    def __or__(self, other):
        ret_func = lambda *dt, **mp: max([self(*dt, **mp), other(*dt, **mp)])
        return ret_func

    def __mul__(self, other):
        ret_func = lambda *dt, **mp: self(*dt, **mp) * other(*dt, **mp)
        return ret_func

    def __call__(self, *dt):
        return self.func(*dt)


class TriFunc(MembershipFunction):
    """
    The triangle membership function.
    """
    def __init__(self, coords=[-1, 0, 1]):
        #self.func = lambda x: 0 if x <= coords[0] else x / (coords[1] - coords[0]) + 1 if x <= coords[1] else x * (-1 / (coords[2] - coords[1])) + 1 if x <= coords[2] else 0
        self.func = lambda x: 0 if x <= coords[0] or x >= coords[2] else (x - coords[0]) / (coords[1] - coords[0]) if x <= coords[1] else 1 - (x - coords[1]) / (coords[2] - coords[1])
