from fuzzpy.memberships import TrapecFunc, TriFunc
from fuzzpy.implications import larsen, mamdani


class FuzzyTerm:
    """
    A fuzzy term like the the weather is hot or the speed is slow
    """
    def __init__(self, membership, variable):
        """
        Create new fuzzy term
        :param membership: The membership function to describe the value of the variable as a fuzzy set
        :param variable: The variable to describe the linguistic term of
        """
        self.membership = membership
        self.variable = variable

    def __call__(self):
        """
        Compute the level
        :return: level
        """
        return self.membership(self.variable.value)

    def __and__(self, other):
        """
        Combine two terms with "and" condition
        :param other: the term to combine with
        :return: new membership function
        """
        def ret_func(*d, **mp):
            a = float(self(*d, **mp))
            b = float(other(*d, **mp))
            return a if a < b else b
        return ret_func

    def __or__(self, other):
        """
        Combine two terms with "or" condition
        :param other: the term to combine with
        :return: new membership function
        """
        def ret_func(*d, **mp):
            a = float(self(*d, **mp))
            b = float(other(*d, **mp))
            return a if a > b else b
        return ret_func


class FuzzyRule:
    """
    A fuzzy rule that works as an membership function
    """
    def __init__(self, antecedents, variable, membership, implication=larsen):
        """
        Create new fuzzy rule
        :param antecedents: A list of (or just the one) antecedents for the rule. Can be associated with different variables
        :param variable: The output variable
        :param membership: The membership function that corresponds to the rule
        :param implication: The implication function that corresponds to the rule
        """
        if isinstance(antecedents, list):
            self.antecedents = antecedents
        else:
            self.antecedents = [antecedents]

        variable.low_limit = min(variable.low_limit, membership.left_border)
        variable.upp_limit = max(variable.upp_limit, membership.right_border)

        self.membership = membership
        self.variable = variable
        self.implication = implication

    def __call__(self, x):
        """
        Compute the ruth level for the given x
        :param x:
        :return:
        """
        self.variable.value = self.implication(self.membership(x), min([cur_ant() for cur_ant in self.antecedents]))
        return self.variable.value


class FuzzyVariable:
    """
    A fuzzy varibale
    """
    def __init__(self):
        self.value = 0.0
        self.low_limit = float("inf")
        self.upp_limit = -float("inf")

    def is_(self, membership):
        """
        Create the fuzzy term associated with the variable
        :param membership: The membership functions that describes the term
        :return: The created fuzzy term
        """
        self.low_limit = min(self.low_limit, membership.left_border)
        self.upp_limit = max(self.upp_limit, membership.right_border)

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

    # check the rules
    for temp in range(0, 35, 5):
        fuzzy_temp.value = temp
        print()
        print("Cur temp = {}".format(temp))
        for freq in range(0, 1001, 100):
            print("Frequency = {}".format(freq))
            print("Fan speed = {}".format(max(blow_slow(freq), blow_fast(freq))))

    print("Temp lower limit is {}".format(fuzzy_temp.low_limit))
    print("Temp upper limit is {}".format(fuzzy_temp.upp_limit))
    print("Blow lower limit is {}".format(fuzzy_blow.low_limit))
    print("Dlow upper limit is {}".format(fuzzy_blow.upp_limit))
