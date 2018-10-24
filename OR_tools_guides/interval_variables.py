"""Code sample to demonstrates how to build an interval."""
from ortools.sat.python import cp_model


def IntervalSample():
    model = cp_model.CpModel()
    horizon = 100
    start_var = model.NewIntVar(0, horizon, 'start')
    duration = 10  # Python cp/sat code accept integer variables or constants.
    end_var = model.NewIntVar(0, horizon, 'end')
    interval_var = model.NewIntervalVar(start_var, duration, end_var, 'interval')
    print('start = %s, duration = %i, end = %s, interval = %s' % (start_var, duration, end_var, interval_var))


if __name__ == '__main__':
    IntervalSample()