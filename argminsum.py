import builtins


# Implementation of argminsum numbers type
class argminsum:
    def __init__(self, val, cnfg):
        self.val = val
        self.cnfg = cnfg

    def __add__(self, other):
        val = self.val + other.val
        if (self.cnfg == set()) or (other.cnfg == set()):
            cnfg = set()
        else:
            cnfg = self.cnfg + other.cnfg
        return argminsum(val, cnfg)

    def __str__(self):
        return f'({self.val},{self.cnfg})'

    def __repr__(self):
        return str(self)


# Override built-ins
def min(u, v):
    if type(u) is not argminsum:
        return builtins.min(u, v)
    else:
        if u.val < v.val:
            return u
        else:
            return v


# Constants
zero = argminsum(0, [])
inf = argminsum(float("inf"), set())