
import sys
sys.path.insert(0, "KachuaCore/interfaces/")
from interfaces.fuzzerInterface import *
import random

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
     
        flag = 0
        #assign flag = 1 if any statement in curr_metric is no in total_metric list
        for i in curr_metric:
            if i not in total_metric:
               flag = 1
               break
        
        if flag  == 1:
            return True
        else:      
            return False

    # TODO : Implement this
    def updateTotalCoverage(self, curr_metric, total_metric):
        # Compute the total_metric coverage and return it (list)
        # this changes if new coverage is seen for a 
        # given input.
        
        #union the total_metric and curr_metric if coverage increases
        total_metric = list(set(total_metric + curr_metric))


        return total_metric

class CustomMutator(MutatorBase):
    def __init__(self):
        pass

    # TODO : Implement this
    def mutate(self, input_data, coverageInfo, irList):
        '''
        Mutate the input data and return it
        coverageInfo is of type CoverageMetricBase
        Don't mutate coverageInfo
        irList : List of IR Statments (Don't Modify)
        input_data.data -> type dict() with {key : variable(str), value : int}
        must return input_data after mutation.
        '''
    

        #Method to Flipping a single bit at random location:
        def f0():
            
            #take input data and after converting it into binary, convert it into list
            input_data.data[value] = list(bin(input_data.data[value]))

            #finding the length of data value
            bl = len(input_data.data[value])
            
            #genarate random number from 2 to len-1 i.e. binary starting from 0b so skip that
            r = random.randint(2, bl-1)
            
            #Flipping single bit at random location r
            if input_data.data[value][r] == '1':
                input_data.data[value][r] = '0'
            else:
                input_data.data[value][r] = '1'

            #convert the list into str so that it can be converted further into integer
            input_data.data[value] = ''.join(map(str, input_data.data[value]))
            
            #convert str to int,int function take two input i.e. data, base (here base =2)
            input_data.data[value] = int(input_data.data[value],2)
                    
            return input_data.data

        #Method to Flip double bit at random location:
        def f1():
            
            #take input data and after converting it into binary, convert it into list
            input_data.data[value] = list(bin(input_data.data[value]))

            #finding the length of data value
            bl = len(input_data.data[value])
                  
            #length of binary data must be greator than 2
            if bl > 3:
                #genarate random number from 2 to len-1 i.e. binary starting from 0b so skip that
                r = random.randint(2, bl-2)

                # Flipping two bits in a row
                if input_data.data[value][r] == '1':
                    input_data.data[value][r] = '0'
                else:
                    input_data.data[value][r] = '1'
                
                r = random.randint(2, bl-2)

                if input_data.data[value][r+1] == '1':
                    input_data.data[value][r+1] = '0'
                else:
                    input_data.data[value][r+1] = '1'          

            #convert the list into str so that it can be converted further into integer
            input_data.data[value] = ''.join(map(str, input_data.data[value]))
           
            #convert str to int,int function take two input i.e. data, base (here base =2)
            input_data.data[value] = int(input_data.data[value],2)

            return input_data.data

        #method that randomly select range from -35 to 35 and add it to input
        def f2():

            #genarate random number ranges -35 to 35
            r = random.randint(-35, 35)

            #update the data value according to r
            input_data.data[value] = input_data.data[value]  + r

            return input_data.data
        
        #method that assign input to a interested inputs
        def f3():

            #defining list of interested inputs i.e. MAX_INT,MIN_INT,MAX_INT-1,MIN_INT+1
            knownint = [-1,0,1,-2147483648,-2147483647,2147483647,2147483648,-9223372036854775808,-9223372036854775807,9223372036854775807,9223372036854775806]
            
            #generate random number from 0 to 10
            r = random.randint(0, 10)

            #assign the interested input to data variable (:x) directly
            input_data.data[value] = knownint[r]

            return input_data.data

        #loop to enumerate the input
        for index,value in enumerate(input_data.data):
            
            #genarate random number from 0 to 3 and according to that call the appropriate function
            m = random.randint(0, 3)
            if m == 0:
                f0()
            elif m == 1:
                f1()
            elif m== 2:
                f2()
            elif m== 3:
                f3()
                
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
