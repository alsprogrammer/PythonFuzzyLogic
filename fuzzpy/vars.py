from fuzzpy.membership import TrapecFunc, TriFunc


class FuzzyTerm:
    def __init__(self, membership, variable):
        self.membership = membership
        self.variable = variable

    def __call__(self):
        return self.membership(self.variable.value)

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


class FuzzyRule:
    def __init__(self, antecedents, variable, membership):
        if isinstance(antecedents, list):
            self.antecedents = antecedents
        else:
            self.antecedents = [antecedents]

        self.membership = membership
        self.variable = variable

    def __call__(self, x):
        self.variable.value = self.membership(x) * min([cur_ant() for cur_ant in self.antecedents])
        return self.variable.value


class FuzzyVariable:
    def __init__(self):
        self.values = []
        self.value = 0.0
        self.low_limit = 0.0
        self.upp_limit = 0.0

    def is_(self, membership):
        self.values.append(membership)
        return FuzzyTerm(membership, self)


if __name__ == "__main__":
    fuzzy_temp = FuzzyVariable()
    hot = TriFunc(20, 25, 50)
    norm = TriFunc(15, 20, 25)
    cold = TrapecFunc(0, 5, 10, 20)

    temp_is_hot = fuzzy_temp.is_(hot)
    temp_is_norm = fuzzy_temp.is_(norm)
    temp_is_cold = fuzzy_temp.is_(cold)

    fuzzy_blow = FuzzyVariable()
    slow = TriFunc(0, 0, 750)
    fast = TriFunc(250, 1000, 1000)

    blow_slow = FuzzyRule(temp_is_cold | temp_is_norm, fuzzy_blow, slow)
    blow_fast = FuzzyRule(temp_is_hot, fuzzy_blow, fast)

    # check the memebership functions and antecedents
    for temp in range(0, 30):
        fuzzy_temp.value = temp
        print("The temp is {}".format(temp))
        print("It's hot: {}".format(temp_is_hot()))
        print("It's norm: {}".format(temp_is_norm()))
        print("It's cold: {}".format(temp_is_cold()))

    # check the rules
    for temp in range(0, 30, 5):
        fuzzy_temp.value = temp
        print()
        print("Cur temp = {}".format(temp))
        for freq in range(0, 1000, 100):
            print("Frequency = {}".format(freq))
            print("Fan speed = {}".format(max(blow_slow(freq), blow_fast(freq))))
