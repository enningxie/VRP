"""Code sample to demonstrates how to build an optional interval."""
from ortools.sat.python import cp_model


def OptionalIntervalSample():
    model = cp_model.CpModel()
    horizon = 100
    start_var = model.NewIntVar(0, horizon, 'start')
    duration = 10
    end_var = model.NewIntVar(0, horizon, 'end')
    presence_var = model.NewBoolVar('presence')
    interval_var = model.NewOptionalIntervalVar(start_var, duration, end_var, presence_var, 'optional_intervals')
    print('start = %s, duration = %i, end = %s, presence = %s, interval = %s' %
          (start_var, duration, end_var, presence_var, interval_var))


if __name__ == '__main__':
    OptionalIntervalSample()