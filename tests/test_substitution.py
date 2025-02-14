from substitution import Substitution


s = Substitution({0: 2, 1: 3, 2: 1, 3: 0, 4: 4})
s2 = Substitution({0: 3, 1: 2, 2: 1, 3: 4, 4: 0})

assert s.order == 10
assert s ** 2 == {0: 1, 1: 0, 2: 3, 3: 2, 4: 4}
assert s ** 3 == {0: 3, 1: 2, 2: 0, 3: 1, 4: 4}
assert s * s2 == {0: 1, 1: 4, 2: 2, 3: 3, 4: 0}
