from substitution import Substitution


s = Substitution({1: 2, 2: 1, 4: 4})

assert str(s.cycles) == "(1 → 2 → 1, 4 → 4)"
assert s.cycles == ((1, 2, 1), (4, 4))
assert s.cycles.count((1, 2, 1)) == 1
