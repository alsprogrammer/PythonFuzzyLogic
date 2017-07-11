from fuzzpy.membership import create_tri

func = create_tri()

for x in range(-4, 5):
    print x / 4.0, func(x / 4.0)
