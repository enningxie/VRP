"""Solves an optimization problem and display all intermediate solutions."""

from ortools.sat.python import cp_model


# You need to subclass the cp_model.CpSolverSolutionCallback class.
class VarArrayAndObjectiveSolutionPrinter(cp_model.CpSolverSolutionCallback):
    """print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def OnSolutionCallback(self):
        self.__solution_count += 1
        print('Solution %i' % self.__solution_count)
        print('objectove value = %i' % self.ObjectiveValue())
        for v in self.__variables:
            print('%s = %i' % (v, self.Value(v)), end=' ')
        print()


    def SolutionCount(self):
        return self.__solution_count


def MinimalCpSatPrintIntermediateSolutions():
    """Showcases printing intermediate solutions found during search."""
    # Creates the model.
    model = cp_model.CpModel()
    # creates the variables.
    num_vals = 3
    x = model.NewIntVar(0, num_vals - 1, 'x')
    y = model.NewIntVar(0, num_vals - 1, 'y')
    z = model.NewIntVar(0, num_vals - 1, 'z')
    # creates the constraints.
    model.Add(x != y)
    # model.Maximize(x + 2 * y + 3 * z)

    # creates a solver and solves.
    solver = cp_model.CpSolver()
    solution_printer = VarArrayAndObjectiveSolutionPrinter([x, y, z])
    status = solver.SearchForAllSolutions(model, solution_printer)

    print('Status = %s' % solver.StatusName(status))
    print('Number of solutions found: %i' % solution_printer.SolutionCount())

if __name__ == '__main__':
    MinimalCpSatPrintIntermediateSolutions()