# prototype/cloneable.py
import copy

class Cloneable:
    def clone(self):
        return copy.deepcopy(self)
