from World import World
from Mandalorian import Mandalorian
class Node(object):
    def __init__(self, state, parent, operator, depth, cost):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost
        
    def getParent(self):
        return self.parent
    
    def getOperator(self):
        return self.operator
    
    def getDepth(self):
        return self.depth
    
    def getCost(self):
        return self.cost
    
    def getState(self):
        return self.state