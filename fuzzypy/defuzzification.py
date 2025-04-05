from typing import Callable, Iterable

from fuzzypy.variables import FuzzyTerm


def step_generator(start: float, stop: float, num: int) -> Iterable[float]:
    if num <= 0:
        raise ValueError("The number of steps shouldn't be zero or negative")
    if start == stop:
        raise ValueError("The start number shouldn't be equal to stop")

    step = float(stop - start) / float(num)
    cur_x = start

    while cur_x <= stop:
        yield cur_x
        cur_x += step


def center_of_gravity(function_to_evaluate: FuzzyTerm, x_elements: Iterable[float]) -> float:
    x = list(x_elements)

    num = sum(
        x * function_to_evaluate(x)
        for x in x
    )

    denum = sum(
        function_to_evaluate(x)
        for x in x
    )

    return num / denum if denum else function_to_evaluate.variable.upp_limit


def defuzzify(term_to_defuzzify: FuzzyTerm, method: Callable[[FuzzyTerm, Iterable[float]], float] = center_of_gravity):
    variable = term_to_defuzzify.variable
    lower_limit = variable.low_limit
    upper_limit = variable.upp_limit

    defuzzified_value = method(term_to_defuzzify, step_generator(lower_limit, upper_limit, 100))

    variable.value = defuzzified_value

    return defuzzified_value
