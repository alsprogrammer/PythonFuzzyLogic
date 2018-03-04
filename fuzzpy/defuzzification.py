def defuzzyfy(rules, defuzzfier):
    variables = {}

    if not isinstance(rules, list):
        items = [rules]
    else:
        items = rules

    for rule in items:
        if id(rule.variable) not in vars:
            variables[id(rule.variable)] = [rule]
        else:
            variables[id(rule.variable)].append(rule)

    for var in variables:
        cur_var = variables[var].variable
