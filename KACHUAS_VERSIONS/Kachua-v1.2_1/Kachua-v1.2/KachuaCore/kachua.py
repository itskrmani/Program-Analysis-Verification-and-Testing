#!/usr/bin/python3

Release="Kachua v1.2"

import sys
import ast

sys.path.insert(0, './parser')
sys.path.insert(0, './ast')
sys.path.insert(0, '../Submission/')

from tlangLexer import tlangLexer
from tlangParser import tlangParser

import kachuaAST
from builder import *
from parseError import *

from submission import *

import antlr4
import argparse
import turtle
import time
import pickle

def IRGenerator(progfl):
    input_stream = antlr4.FileStream(progfl)
    print(input_stream)
    try:
        lexer = tlangLexer(input_stream)
        stream = antlr4.CommonTokenStream(lexer)
        lexer._listeners = [SyntaxErrorListener()]
        parser = tlangParser(stream)
        parser._listeners = [SyntaxErrorListener()]
        tree = parser.start()
    except Exception as e :
        print('\033[91m\n====================')
        print(e.__str__() + '\033[0m\n')
        exit(1)

    # instantiate visitor
    astgen = astGenPass()
    irlist = astgen.visitStart(tree)
    return irlist

def pretty_print(ir):
    print('========== IR ==========\n')
    for idx, item in enumerate(ir):
        print(idx, item[0], ' [', item[1], ']')

def addContext(s):
    return str(s).strip().replace(":", "self.prg.")


# TODO: move to a different file
class Interpreter:
# Turtle program should not contain variable with names "ir", "pc", "t_screen"
    ir = None
    pc = None
    t_screen = None
    trtl = None

    def __init__(self, ir):
        self.ir = ir
        self.pc = 0
        self.t_screen = turtle.getscreen()
        self.trtl = turtle.Turtle()
        self.trtl.shape("turtle")
        self.trtl.color("brown")
        self.trtl.fillcolor("green")
        self.trtl.speed(1) # TODO: Make it user friendly
        turtle.title(Release)
        turtle.hideturtle()
        
    def initProgramContext(self, params):
        for key,val in params.items():
            var = key.replace(":","")
            exec("setattr(self.prg,\"%s\",%s)" % (var, val))
        
    def handleAssignment(self, stmt,tgt):
        raise NotImplementedError('Assignments are not handled!')

    def handleCondition(self, stmt, tgt):
        raise NotImplementedError('Conditions are not handled!')

    def handleMove(self, stmt, tgt):
        raise NotImplementedError('Moves are not handled!')

    def handlePen(self, stmt, tgt):
        raise NotImplementedError('Pens are not handled!')

    def handleGotoCommand(self, stmt, tgt):
        raise NotImplementedError('Gotos are not handled!')

    def interpret(self):
        if self.pc >= len(self.ir):
            return True # program terminated

        print("Program counter : ", self.pc)
        stmt, tgt = self.ir[self.pc]
        print(stmt, stmt.__class__.__name__,tgt)

        if isinstance(stmt, kachuaAST.AssignmentCommand):
            ntgt = self.handleAssignment(stmt, tgt)
        elif isinstance(stmt, kachuaAST.ConditionCommand):
            ntgt = self.handleCondition(stmt, tgt)
        elif isinstance(stmt, kachuaAST.MoveCommand):
            ntgt = self.handleMove(stmt, tgt)
        elif isinstance(stmt, kachuaAST.PenCommand):
            ntgt = self.handlePen(stmt, tgt)
        elif isinstance(stmt, kachuaAST.GotoCommand):
            ntgt = self.handleGotoCommand(stmt, tgt)
        else:
            raise NotImplementedError("Unknown instruction: %s, %s."%(type(stmt), stmt))

        # TODO: handle statement
        self.pc += ntgt
        return True if self.pc > len(self.ir) else False # TODO: return termination status

class ProgramContext:
    pass

# TODO: move to a different file
class ConcreteInterpreter(Interpreter):
    # Ref: https://realpython.com/beginners-guide-python-turtle
    cond_eval = None # used as a temporary variable within the embedded program interpreter
    prg = None

    def __init__(self, ir):
        super().__init__(ir)
        self.prg = ProgramContext()
        
    def handleAssignment(self, stmt, tgt):
        print("  Assignment Statement")
        lhs = str(stmt.lvar).replace(":","")
        rhs = addContext(stmt.rexpr)
        exec("setattr(self.prg,\"%s\",%s)" % (lhs,rhs))
        return 1

    def handleCondition(self, stmt, tgt):
        print("  Branch Instruction")
        condstr = addContext(stmt)
        exec("self.cond_eval = %s" % (condstr))
        return 1 if self.cond_eval else tgt

    def handleMove(self, stmt, tgt):
        print("  MoveCommand")
        exec("self.trtl.%s(%s)" % (stmt.direction,addContext(stmt.expr)))
        return 1

    def handlePen(self, stmt, tgt):
        print("  PenCommand")
        exec("self.trtl.%s()"%(stmt.status))
        return 1

    def handleGotoCommand(self, stmt, tgt):
        print(" GotoCommand")
        xcor = addContext(stmt.xcor)
        ycor = addContext(stmt.ycor)
        exec("self.trtl.goto(%s, %s)" % (xcor, ycor))
        return 1

def interpret(ir, params={}):
    # for stmt,pc in ir:
    #     print(str(stmt.__class__.__bases__[0].__name__),pc)
    inptr = ConcreteInterpreter(ir)
    terminated = False
    inptr.initProgramContext(params)
    while True:
        terminated = inptr.interpret()
        if terminated:
            break
    print("Program Ended.")


def cleapup():
    pass

def stopTurtle():
    turtle.bye()

def dumpIR(filename, ir):
    with open(filename, 'wb') as f:
        pickle.dump(ir, f)

def loadIR(filename):
    f = open(filename, 'rb')
    ir = pickle.load(f)
    return ir


if __name__ == '__main__':

    print(Release)
    print("------------")

    # process the command-line arguments
    cmdparser = argparse.ArgumentParser(description='Program Analysis Framework for Turtle.')

    # add arguments for parsing command-line arguments
    cmdparser.add_argument('-p', '--ir', action='store_true', help='pretty printing')
    cmdparser.add_argument('-r', '--run', action='store_true', help='execute program')
    cmdparser.add_argument('-O', '--opt', action='store_true', help='optimize')
    cmdparser.add_argument('-b', '--bin', action='store_true', help='load binary IR')
    cmdparser.add_argument('progfl')

    # passing variable values via command line. E.g.
    # ./kachua.py -r <program file> --params '{":x" : 10, ":z" : 20, ":w" : 10, ":k" : 2}'
    cmdparser.add_argument('-d', '--params', default={},  type=ast.literal_eval, help="pass variable values to kachua program in python dictionary format")
    # TODO: add additional arguments for parsing command-line arguments

    args = cmdparser.parse_args()
    
    if not (type(args.params) is dict):
        raise ValueError("Wrong type for command line arguement '-d' or '--params'.")

    # generate IR
    if args.bin:
        ir = loadIR(args.progfl)
    else:
        ir = IRGenerator(args.progfl)

    if args.ir:
        pretty_print(ir)

    if True:
        cfg = genCFG(ir)
        dumpCFG(cfg)

    if args.opt:
        ir2 = optimize(ir)
        dumpIR("optimized.kw", ir2)

    if args.run:
        interpret(ir, args.params)
        print()
        print("Press ESCAPE to exit")
        turtle.listen()
        turtle.onkeypress(stopTurtle, "Escape")
        turtle.mainloop()
        #print()
        # input("Press Enter to continue...")
