import csp

p = csp.Problem()

# 3SAT - 1
p.create_and_add_variable('a', [True, False])
p.create_and_add_variable('b', [True, False])
p.create_and_add_variable('c', [True, False])
p.create_and_add_variable('d', [True, False])
p.create_and_add_variable('e', [True, False])
p.create_and_add_variable('f', [True, False])

p.create_and_add_constraint(lambda x, y: (x or y) is True, ['e', 'f'])
p.create_and_add_constraint(lambda x, y, z: (y or (x and z)) is True, ['a', 'b', 'c'])
p.create_and_add_constraint(lambda x, y, z: (z or (x and not y and not z)) is True, ['b', 'e', 'f'])
p.create_and_add_constraint(lambda x, y, z, w, t, k: ((not x and y and w and (k or not z)) or
                                                      (x and (w or not z or t or x))) is True,
                            ['a', 'b', 'c', 'd', 'e', 'f'])

"""
# 3SAT - 2
p.create_and_add_variable('K', [True, False])
p.create_and_add_variable('L', [True, False])
p.create_and_add_variable('M', [True, False])
p.create_and_add_variable('N', [True, False])
p.create_and_add_variable('T', [True, False])

p.create_and_add_constraint(lambda x, y, z, w, v: (v or not (not x or y or z or not w) or
                                                   ((z and x) or (w and z) or (not v and y))) is True,
                            ['K', 'L', 'M', 'N', 'T'])
p.create_and_add_constraint(lambda x, y: ((y and x) or (not x and not y)) is True, ['L', 'M'])
"""

"""
# 3SAT - 3
p.create_and_add_variable('P', [True, False])
p.create_and_add_variable('Q', [True, False])
p.create_and_add_variable('R', [True, False])

p.create_and_add_constraint(lambda x, y, z: (not (not x and (z or not y)) or not (z and not y)) is True,
                            ['P', 'Q', 'R'])
p.create_and_add_constraint(lambda x, y, z: ((not x and (not y or z)) or (z and not y)) is True,
                            ['P', 'Q', 'R'])
p.create_and_add_constraint(lambda x, y, z: (x or z or not y) is True,
                            ['P', 'Q', 'R'])
p.create_and_add_constraint(lambda x, y: (y or (not x and y)) is True,
                            ['P', 'Q'])
"""

"""
# 3SAT - 4
p.create_and_add_variable('x', [True, False])
p.create_and_add_variable('y', [True, False])
p.create_and_add_variable('z', [True, False])
p.create_and_add_variable('w', [True, False])

p.create_and_add_constraint(lambda a, b, c, d: (c or (d and not b and (not a or b))) is True,
                            ['x', 'y', 'z', 'w'])
p.create_and_add_constraint(lambda a, b, c: (a or not (b or c)) is True,
                            ['x', 'y', 'z'])
p.create_and_add_constraint(lambda a, b, c: (not a or (b and a and not c)) is True,
                            ['x', 'y', 'z'])
p.create_and_add_constraint(lambda a, b, c, d: (c or d or (not a or b)) is True,
                            ['x', 'y', 'z', 'w'])
p.create_and_add_constraint(lambda a, b, c, d: (d or b or not a or (d and c)) is True,
                            ['x', 'y', 'z', 'w'])
"""

"""
# 3SAT - 5
p.create_and_add_variable('x', [True, False])
p.create_and_add_variable('y', [True, False])
p.create_and_add_variable('z', [True, False])
p.create_and_add_variable('p', [True, False])
p.create_and_add_variable('q', [True, False])
p.create_and_add_variable('r', [True, False])

p.create_and_add_constraint(lambda a, c, e: (c and e and a) is True,
                            ['x', 'z', 'q'])
p.create_and_add_constraint(lambda a, b, d, e: ((a and d) or (not e or a) or (d and b)) is True,
                            ['x', 'y', 'p', 'q'])
p.create_and_add_constraint(lambda a, b, c, f: ((c and b) or (a and not f)) is True,
                            ['x', 'y', 'z', 'r'])
p.create_and_add_constraint(lambda b, c, d: (not b or not c or d) is True,
                            ['y', 'z', 'p'])
p.create_and_add_constraint(lambda a, b, c, d, f: (a or not b or (c and d and f)) is True,
                            ['x', 'y', 'z', 'p', 'r'])
p.create_and_add_constraint(lambda a, c, d, f: ((a and d and c) or not f) is True,
                            ['x', 'z', 'p', 'r'])
p.create_and_add_constraint(lambda b, f: (b or f) is True,
                            ['y', 'r'])
"""

# bt_solutions = p.get_all_solutions('bt')               # backtracking

fc_solutions = p.get_all_solutions('fc')              # forward checking
print(*fc_solutions[0], sep="\n")
