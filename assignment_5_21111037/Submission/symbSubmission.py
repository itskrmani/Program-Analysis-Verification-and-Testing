from z3 import *
import argparse
import json
import sys
sys.path.insert(0, '../KachuaCore/')
from sExecutionInterface import *
import z3solver as zs
from irgen import *
from interpreter import *
import ast

def example(s):
    # To add symbolic variable x to solver
    s.addSymbVar('x')
    s.addSymbVar('y')
    # To add constraint in form of string
    s.addConstraint('x==5+y')
    s.addConstraint('And(x==y,x>5)')
    # s.addConstraint('Implies(x==4,y==x+8')
    # To access solvers directly use s.s.<function of z3>()
    print("constraints added till now",s.s.assertions())
    # To assign z=x+y
    s.addAssignment('z','x+y')
    # To get any variable assigned
    print("variable assignment of z =",s.getVar('z'))



#Method to interpret the intermediate reprsentation and return the object of ConcreteInterpreator class
def interpret(ir, params={}):
    
    #call ConcreteInterpreator method which is implemented in Interpreter file
    inptr = ConcreteInterpreter(ir)

    terminated = False
    inptr.initProgramContext(params)
    while True:
        terminated = inptr.interpret()
        if terminated:
            break
        
    return inptr



#Method to check two given program are equivalent or not
#Take Two parameters 
# args => take input arguments from user given in -e flag
# ir => Intermediate representation
def checkEq(args,ir):

    #Open Json file in read mode 
    file1 = open("../Submission/testData.json","r+")

    # convert testData.json datatype from str to dict 
    testData=json.loads(file1.read())

    #now close the testData.json file
    file1.close()
    s = zs.z3Solver()
    testData = convertTestData(testData)
    # TODO: write code to check equivalence
   
    #iterate the testdata which is of a dict type
    for indx in testData:
        
        #fetch all the paramters value from the testdata file
        myinptr = interpret(ir,testData[indx]['params'])
       
        #fetch all the SymbEnc value from the testdata file
        val = ast.literal_eval(testData[indx]['symbEnc'])
    
        #Iterate parameters from the testdata file with the help of Indx and params
        for m in testData[indx]['params']:
            # To add all the symbolic variable m to solver
            s.addSymbVar(m)


        for m in val:
            for n in args.output:
                #Replace all the args seeded from the user with their corresponding Symbolic value
                val[m] = val[m].replace(str(n), str(testData[indx]['params'][n]))
    
         
        for i in args.output:
            # Constraint to Equate the user seeded value with their corresponding value already we have
            s.addConstraint(val[i] + '==' + str(getattr(myinptr.prg, i)))
    
    print(myinptr)
    print(s.s.assertions())
    # Check if solver return "sat" , if it is that means solution to the entered equation have exists
    if(str(s.s.check())=='sat'):
        print(s.s.model())
    else:
        print("Both Programs are Unequal")
    
    



if __name__ == '__main__':
    cmdparser = argparse.ArgumentParser(
        description='symbSubmission for assignment Program Synthesis using Symbolic Execution')
    cmdparser.add_argument('progfl')
    cmdparser.add_argument(
        '-b', '--bin', action='store_true', help='load binary IR')
    cmdparser.add_argument(
        '-e', '--output', default=list(), type=ast.literal_eval,
                               help="pass variables to kachua program in python dictionary format")
    args = cmdparser.parse_args()
    ir = loadIR(args.progfl)
    checkEq(args,ir)
    exit()
