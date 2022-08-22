
import sys
sys.path.insert(0, "KachuaCore/interfaces/")
from interfaces.fuzzerInterface import *

# make sure dot or xdot works and grapviz is installed.

# Uncomment for Assignment-2
# sys.path.append("KachuaCore/kast")
# import kast.kachuaAST
# import graphviz

class CustomCoverageMetric(CoverageMetricBase):
    # Statements covered is used for 
    # coverage information.
    def __init__(self):
        super().__init__()

    # TODO : Implement this
    def compareCoverage(self, curr_metric, total_metric):
        # must compare curr_metric and total_metric
        # True if Improved Coverage else False
        return False

class CustomMutator(MutatorBase):
    def __init__(self):
        pass

    # TODO : Implement this
    def mutate(self, input_data):
        # Mutate the input data and return it
        # input_data.data -> type dict() with {key : variable(str), value : int}
        # must return input_data after mutation.
        return input_data

# Reuse code and imports from 
# earlier submissions (if any).
def genCFG(ir):
    # your code here
    cfg = None
    return cfg

def dumpCFG(cfg):
    # dump CFG to a dot file
    pass

def optimize(ir):
    # create optimized ir in ir2
    ir2 = ir # currently no oprimization is enabled
    return ir2
