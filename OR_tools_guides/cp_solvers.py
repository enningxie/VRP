# Three variables, x, y, and z, each of which can take on the values: 0, 1, or 2.
# One constraint: x ≠ y

# 1. declare the solver
from ortools.sat.python import cp_model
import collections


class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    '''Print intermediate'''
    def __init__(self, variables):
        self.__variables = variables
        self.__solution_count = 0

    def NewSolution(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('{} = {}'.format(v, self.Value(v)), end=' ')
        print()

    def SolutionCount(self):
        return self.__solution_count


def main():
    # create the model and solver
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()

    # create the variables
    num_vals = 3
    x = model.NewIntVar(0, num_vals - 1, 'x')
    y = model.NewIntVar(0, num_vals - 1, 'y')
    z = model.NewIntVar(0, num_vals - 1, 'z')

    # create the constraint
    model.Add(x != y)

    # call the solver.
    solution_printer = SolutionPrinter([x, y, z])
    status = solver.SearchForAllSolutions(model, solution_printer)

    # create the solution printer
    print('Number of solutions found: {}'.format(solution_printer.SolutionCount()))


if __name__ == '__main__':
    main()