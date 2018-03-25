def step_generator(start, stop, num):
    if num <= 0:
        raise ValueError("The number of steps shouldn't be zero or negative")
    if start == stop:
        raise ValueError("The start number shouldn't be equal to stop")
    step = float(stop - start) / float(num)
    cur_x = start
    while cur_x <= stop:
        yield cur_x
        cur_x += step


def prec_generator(start, stop, step):
    if step == 0:
        raise ValueError("The steps value shouldn't be zero")
    if start == stop:
        raise ValueError("The start number shouldn't be equal to stop")
    cur_x = start
    while cur_x <= stop:
        yield cur_x
        cur_x += step


def apply_defuzzyfy_COG(rules):
    variables = {}
    ret_vals = []

    if isinstance(rules, list):
        items = rules
    else:
        items = [rules]

    for rule in items:
        if id(rule.variable) not in variables:
            variables[id(rule.variable)] = [rule]
        else:
            variables[id(rule.variable)].append(rule)

    for var in variables:
        cur_var = variables[var][0].variable
        upp = 0
        bott = 0
        for x in step_generator(cur_var.low_limit, cur_var.upp_limit, 100):
            mu = max([fuzzy_val(x) for fuzzy_val in variables[var]])
            upp += (x * mu)
            bott += mu
        cur_var.value = upp / bott
        ret_vals.append(cur_var.value)

    return ret_vals
