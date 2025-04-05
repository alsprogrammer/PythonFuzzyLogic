__version__ = '1.0'

from fuzzypy.defuzzification import defuzzify
from fuzzypy.memberships import TriFunc, TrapecFunc
from fuzzypy.variables import FuzzyVariable, FuzzyRule, build_resulting_fuzzy_term

if __name__ == "__main__":
    # Create a fuzzy variable
    fuzzy_temp = FuzzyVariable()  # Temperature

    # Define the membership functions
    hot = TriFunc(20, 25, 50)
    norm = TriFunc(15, 20, 25)
    cold = TrapecFunc(0, 5, 10, 20)

    # Determine the fuzzy terms
    temp_is_hot = fuzzy_temp.is_(hot)  # The temperature is hot
    temp_is_norm = fuzzy_temp.is_(norm)  # The temperature is normal
    temp_is_cold = fuzzy_temp.is_(cold)  # The temperature is cold

    # Create an output fuzzy variable
    fuzzy_blow = FuzzyVariable()  # The speed of the fan

    # and its membership functions
    slow = TriFunc(0, 0, 750)
    fast = TriFunc(250, 1000, 1000)

    # Determine the rules
    rules = [
        FuzzyRule(temp_is_cold | temp_is_norm, fuzzy_blow, slow),  # If the temperature is cold or normal then fan speed is slow
        FuzzyRule(temp_is_hot, fuzzy_blow, fast),  # If the temperature is hot then fan speed is fast
    ]

    fuzzy_temp.value = 30  # Let the temperature be 30 degrees

    # Let's find the limits of the variables
    print("Temp lower limit is {}".format(fuzzy_temp.low_limit))
    print("Temp upper limit is {}".format(fuzzy_temp.upp_limit))
    print("Blow lower limit is {}".format(fuzzy_blow.low_limit))
    print("Blow upper limit is {}".format(fuzzy_blow.upp_limit))

    print("The temperature is {}".format(fuzzy_temp.value))
    fuzzy_fan_speed = build_resulting_fuzzy_term(rules, fuzzy_blow)
    fan_speed = defuzzify(fuzzy_fan_speed)  # the default method is center-of-gravity

    print("Defuzzyfied values are {}".format(fan_speed))  # it could be more then one value
    print("Or defuzzyfied fan speed is {}".format(fuzzy_blow.value))  # and we can check the value of the fan speed

    # directly
    fuzzy_temp.value = 14  # and now the temp is 13 degrees
    fuzzy_fan_speed = build_resulting_fuzzy_term(rules, fuzzy_blow)
    defuzzify(fuzzy_fan_speed)  # no explicit defuzzified value, but we have it in the variable
    print("Now the temperature is {}, and the fan speed is {}".format(fuzzy_temp.value, fuzzy_blow.value))  # and print it
