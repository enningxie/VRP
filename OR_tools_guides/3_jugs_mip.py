from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ortools.sat.python import cp_model


class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
  """Print intermediate solutions."""

  def __init__(self, variables):
    cp_model.CpSolverSolutionCallback.__init__(self)
    self.__variables = variables
    self.__solution_count = 0

  def OnSolutionCallback(self):
    self.__solution_count += 1
    for v in self.__variables:
      print('%s=%i' % (v, self.Value(v)), end=' ')
    print()

  def SolutionCount(self):
    return self.__solution_count


def ChannelingSample():
  """Demonstrates how to link integer constraints together."""

  # Model.
  model = cp_model.CpModel()

  # Variables.
  x = model.NewIntVar(0, 10, 'x')
  y = model.NewIntVar(0, 10, 'y')

  b = model.NewBoolVar('b')

  # Implement b == (x >= 5).
  model.Add(x >= 5).OnlyEnforceIf(b)
  model.Add(x < 5).OnlyEnforceIf(b.Not())

  # b implies (y == 10 - x).
  model.Add(y == 10 - x).OnlyEnforceIf(b)
  # not(b) implies y == 0.
  model.Add(y == 0).OnlyEnforceIf(b.Not())

  # Search for x values in increasing order.
  model.AddDecisionStrategy([x], cp_model.CHOOSE_FIRST,
                            cp_model.SELECT_MIN_VALUE)

  # Create a solver and solve with a fixed search.
  solver = cp_model.CpSolver()

  # Force solver to follow the decision strategy exactly.
  # solver.parameters.search_branching = cp_model.pywrapsat

  # Searches and prints out all solutions.
  solution_printer = VarArraySolutionPrinter([x, y, b])
  solver.SearchForAllSolutions(model, solution_printer)
  solution_printer.OnSolutionCallback()
  print(solution_printer.SolutionCount())


ChannelingSample()