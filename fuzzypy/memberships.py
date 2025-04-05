from typing import Callable


class MembershipFunction:
    """
    Abstract class for creating of Membership function.
    The functions can be multiplied, also "and" and "or" operators are applicable
    """
    func: Callable[[float], float]

    def __init__(self, *args):
        self.__points = sorted(args[0] if isinstance(args, tuple) and len(args) ==  1 else args)
        self.left_border = min(self.__points)
        self.right_border = max(self.__points)

    def __and__(self, other: "MembershipFunction") -> "MembershipFunction":
        ret = MembershipFunction(list(set(self.__points).union(set(other.__points))))

        def ret_func(*d, **mp):
            return min(float(self(*d, **mp)), float(other(*d, **mp)))

        ret.func = ret_func

        return ret

    def __or__(self, other: "MembershipFunction") -> "MembershipFunction":
        ret = MembershipFunction(list(set(self.__points).union(set(other.__points))))

        def ret_func(*d, **mp) -> float:
            return max(float(self(*d, **mp)), float(other(*d, **mp)))

        ret.func = ret_func

        return ret

    def __mul__(self, other: "MembershipFunction") -> "MembershipFunction":
        ret = MembershipFunction(list(set(self.__points).union(set(other.__points))))

        def ret_func(*d, **mp) -> float:
            return float(self(*d, **mp)) * float(other(*d, **mp))

        ret.func = ret_func

        return ret

    def __call__(self, x: float) -> float:
        return self.func(x)


class TriFunc(MembershipFunction):
    """
    The triangle membership function.
    """
    def __init__(self, *args):
        super(TriFunc, self).__init__(*args)

        def trifunc(x: float) -> float:
            if x < args[0]:
                ret = 0.0
            elif x <= args[1] != args[0]:
                ret = (x - args[0]) / (args[1] - args[0])
            elif x <= args[2]:
                ret = 1 - (x - args[1]) / (args[2] - args[1])
            else:
                ret = 0.0
            return ret

        self.func = trifunc


class TrapecFunc(MembershipFunction):
    """
    The triangle membership function.
    """
    def __init__(self, *args):
        super(TrapecFunc, self).__init__(*args)

        def trapfunc(x: float) -> float:
            if x < args[0]:
                ret = 0.0
            elif x <= args[1]:
                ret = (x - args[0]) / (args[1] - args[0])
            elif x <= args[2]:
                ret = 1
            elif x <= args[3]:
                ret = 1 - (x - args[2]) / (args[3]- args[2])
            else:
                ret = 0.0

            return ret

        self.func = trapfunc
