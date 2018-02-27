class TriFunc(object):
    def __init__(self, coords=[-1, 0, 1]):
        self.func = lambda x: 0 if x <= coords[0] else x / (coords[1] - coords[0]) + 1 if x < coords[1] else x * (-1 / (coords[2] - coords[1])) + 1 if x <= coords[2] else 0

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


def create_tri(coords=[-1, 0, 1]):
    ret = lambda x: 0 if x <= coords[0] else x / (coords[1] - coords[0]) + 1 if x < coords[1] else x * (-1 / (coords[2] - coords[1])) + 1 if x <= coords[2] else 0
    return ret
