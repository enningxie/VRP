"""Simple solve."""
from ortools.sat.python import cp_model


def SimpleSolve():
    """Minimal CP-SAT example to showcase calling the solver."""
    # creates the model.
    model = cp_model.CpModel()
    # creates the variables.
    num_vals = 3
    x = model.NewIntVar(0, num_vals - 1, 'x')
    y = model.NewIntVar(0, num_vals - 1, 'y')
    z = model.NewIntVar(0, num_vals - 1, 'z')
    # creates the constraints.
    model.Add(x != y)

    # creates a solver and solves the model.
    solver = cp_model.CpSolver()

    # sets a time limit of 10 seconds.
    solver.parameters.max_time_in_seconds = 10.0

    status = solver.Solve(model)

    if status == cp_model.FEASIBLE:
        print('x = %i' % solver.Value(x))
        print('y = %i' % solver.Value(y))
        print('z = %i' % solver.Value(z))


if __name__ == '__main__':
    SimpleSolve()