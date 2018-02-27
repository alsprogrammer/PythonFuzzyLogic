from fuzzpy.membership import create_tri, TriFunc

func1 = create_tri()
func2 = TriFunc()
func3 = TriFunc([0, 1, 2])
func4 = func2 and func3

for x in range(-4, 10):
    print(x / 4.0, func2(x / 4.0))
    print(x / 4.0, func3(x / 4.0))
    print(x / 4.0, func4(x / 4.0))
