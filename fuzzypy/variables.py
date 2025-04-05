from collections.abc import Callable
from typing import Union, Iterable, Any, Optional

from fuzzypy.memberships import MembershipFunction
from fuzzypy.implications import larsen, mamdani


class FuzzyTerm:
    """
    A fuzzy term like the weather is hot or the speed is slow
    """
    def __init__(self, membership: Union[MembershipFunction, Callable[[Any], float]], variable):
        """
        Create new fuzzy term
        :param membership: The membership function to describe the value of the variable as a fuzzy set
        :param variable: The variable to describe the linguistic term of
        """
        self.membership = membership
        self.variable = variable

    def __call__(self, optional_x: Optional[float] = None):
        """
        Compute the level
        :return: level
        """
        return self.membership(optional_x if optional_x is not None else self.variable.value)

    def __and__(self, other):
        """
        Combine two terms with "and" condition
        :param other: the term to combine with
        :return: new membership function
        """
        def ret_func(*d, **mp) -> float:
            return min(float(self.membership(*d, **mp)), float(other.membership(*d, **mp)))

        ret_term = FuzzyTerm(ret_func, self.variable)

        return ret_term

    def __or__(self, other):
        """
        Combine two terms with "or" condition
        :param other: the term to combine with
        :return: new membership function
        """
        def ret_func(*d, **mp) -> float:
            return max(float(self.membership(*d, **mp)), float(other.membership(*d, **mp)))

        ret_term = FuzzyTerm(ret_func, self.variable)

        return ret_term


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


def build_resulting_fuzzy_term(rules: Union[FuzzyRule, Iterable[FuzzyRule]], variable_to_build_for: FuzzyVariable) -> FuzzyTerm:
    if not isinstance(rules, list):
        rules = [rules]

    given_variable_rules = [
        rule
        for rule in rules
        if rule.variable == variable_to_build_for
    ]

    def resulting_membership_function(x):
        return max(
            [
                rule(x)
                for rule in given_variable_rules
            ]
        )

    return FuzzyTerm(resulting_membership_function, variable_to_build_for)
