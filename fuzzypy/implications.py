def larsen(member_value: float, alfa_level: float) -> float:
    return member_value * alfa_level


def mamdani(member_value: float, alfa_level: float) -> float:
    return min(member_value, alfa_level)
