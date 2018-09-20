import sys
from ortools.constraint_solver import pywrapcp


# Boolean combinations for two statments:
# A: x != y
# B: y != z
boolean_combs = ['A_and_B', 'A_or_B']


def main(comb):
    # creates the solver.
    solver = pywrapcp.Solver('simple_example')
    # create the variables.
    num_vals = 3
    x = solver.IntVar(0, num_vals - 1, 'x')
    y = solver.IntVar(0, num_vals - 1, 'y')
    z = solver.IntVar(0, num_vals - 1, 'z')

    # create the constraints.
    label = ''  # Label for displaying results.

    if comb is 'A_and_B':
        # Combine constraints by "and".
        solver.Add(x != y)
        solver.Add(y != z)
        label = 'Solution for which x != y and y != z:'

    elif comb is 'A_or_B':
        # Combine constraints by "or".
        solver.Add(solver.Max(x != y, y != z) == 1)
        label = 'Solutions for which x != y or y != z:'

    # create the decision builder.
    db = solver.Phase([x, y, z], solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)
    solver.Solve(db)
    print(label)
    print()

    count = 0
    while solver.NextSolution():
        count += 1
        print('Solution', count, '\n')
        print('x = ', x.Value())
        print('y = ', y.Value())
        print('z = ', z.Value())
        print()
    print('Number of solutions: ', count)


if __name__ == '__main__':
    for comb in boolean_combs:
        main(comb)