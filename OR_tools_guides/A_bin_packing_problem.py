"""Solves a binpacking problem."""

from ortools.sat.python import cp_model


def BinpackingProblem():
    """Solves a bin-packing problem."""
    # Data
    bin_capacity = 100
    slack_capacity = 20
    num_bins = 5
    all_bins = range(num_bins)

    items = [(20, 6), (15, 6), (30, 4), (45, 3)]
    num_items = len(items)
    all_items = range(num_items)

    # model.
    model = cp_model.CpModel()

    # main variables.
    x = {}
    for i in all_items:
        num_copies = items[i][1]
        for b in all_bins:
            x[(i, b)] = model.NewIntVar(0, num_copies, 'x_%i_%i' % (i, b))

    # Load variables.
    load = [model.NewIntVar(0, bin_capacity, 'load_%i' % b) for b in all_bins]

    # Slack variables.
    slacks = [model.NewBoolVar('slack_%i' % b) for b in all_bins]

    # Links load and x.
    for b in all_bins:
        model.Add(load[b] == sum(x[(i, b)] * items[i][0] for i in all_items))

    # place all items.
    for i in all_items:
        model.Add(sum(x[(i, b)] for b in all_bins) == items[i][1])

    # Links load and slack through an equivalence relation.
    safe_capacity = bin_capacity - slack_capacity

    for b in all_bins:
        # slacks[b] => load[b] <= safe_capacity.
        model.Add(load[b] <= safe_capacity).OnlyEnforceIf(slacks[b])
        # not(slacks[b]) => load[b] > safe_capacity.
        model.Add(load[b] > safe_capacity).OnlyEnforceIf(slacks[b].Not())


    # Maximize sum of slacks.
    model.Maximize(sum(slacks))

    # Solves and prints out the solution.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    print('Solve status: %s' % solver.StatusName(status))
    if status == cp_model.OPTIMAL:
        print('Optimal objective value: %i' % solver.ObjectiveValue())
        for i in all_items:
            for b in all_bins:
                if solver.Value(x[(i, b)]):
                    print('{} {}: {}'.format(i, b, solver.Value(x[(i, b)])))
    print('Statistics')
    print('  - conflicts : %i' % solver.NumConflicts())
    print('  - branches : %i' % solver.NumBranches())
    print('  - wall time : %i' % solver.WallTime())




if __name__ == '__main__':
    BinpackingProblem()