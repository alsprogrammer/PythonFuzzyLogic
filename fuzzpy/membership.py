def create_tri(coords=[-1, 0, 1]):
    ret = lambda x: 0 if x <= coords[0] else x / (coords[1] - coords[0]) + 1 if x < coords[1] else x * (-1 / (coords[2] - coords[1])) + 1 if x <= coords[2] else 0
    return ret
