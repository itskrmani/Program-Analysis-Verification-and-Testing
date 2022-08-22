
import sys
sys.path.insert(0, "KachuaCore/interfaces/")
from interfaces.fuzzerInterface import *


sys.path.insert(0, '../KachuaCore/ast')
# from supported import *
import kachuaAST 
import irgen


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
    

def optimize(ir):
    # create optimized ir in ir2
    ir2 = genCFG(ir) # currently no oprimization is enabled
    # for key,val in enumerate(ir2):
    #      print(key,val[0],"first")
      
    redundant =[]
    penst = []
    mylen = 0
    ps = "d"
    # print("\n====This is to find penstatus move====")
    for i in range(len(ir2)):
        # print("\n==>> block",i)
        for j in range(len(ir2[i])):
            
            #Code for finding status of pen i.e. pendown/penup
            if isinstance(ir2[i][j][1], kachuaAST.PenCommand):
                if ir2[i][j][1].status == 'penup':
                    ps = "u"
                    penst.insert(ir2[i][j][0],ps)
                if ir2[i][j][1].status == 'pendown':
                    ps = "d"
                    penst.insert(ir2[i][j][0],ps)
            else:
                penst.insert(ir2[i][j][0],ps)
        
            # print(ir2[i][j][0],ir2[i][j][1],ir2[i][j][2],"==>",penst[ir2[i][j][0]])
    

    # total no of statements count 
    ini = 0
    r = "n"
    myflag = 0
    # print(penst)
    
    penst.reverse()
    # print(penst)
    # print("\n====This is to find redundant move====")
    for i in reversed(range(len(ir2))):
        # print("\n==>> block",i)
        for j in reversed(range(len(ir2[i]))):
            
            #Code for finding reduntant move command
            if isinstance(ir2[i][j][1], kachuaAST.MoveCommand) and ((myflag == 1)  and penst[ir2[i][j][0]] == 'u' and  (ir2[i][j][1].direction == 'forward' or ir2[i][j][1].direction == 'backward')):
                # penst[mylen - ir2[i][j][0]] == 'u' and 
                
                    r = 'r'
                    
                    redundant.insert(ini,r)
                    ini += 1
                    # print(ini,redundant[ini],"hello world")
                    
                    
            else:
                r = 'n'
                
                redundant.insert(ini,r)
                ini += 1
                
                # print("hello3",ir2[i][j][0])
                    
            if isinstance(ir2[i][j][1], kachuaAST.MoveCommand) and myflag == 0:
                if ir2[i][j][1].direction == 'forward' or ir2[i][j][1].direction == 'backward' :
                    myflag = 1

                    # print("hello2",ir2[i][j][0])
           
            if (isinstance(ir2[i][j][1], kachuaAST.GotoCommand) or str(ir2[i][j][1]) == "False") and myflag == 1:
                r = 'n'

            
            # print(ir2[i][j][0],ir2[i][j][1],ir2[i][j][2],"==>",redundant[ini-1])
        
    penst.reverse()
    redundant.reverse()
    # print(redundant)
    # print(penst)
    myflag2 = 0
    myini = 0
    myi = -3
    
    print("\n====Optimize move statements====")

    for key,val in enumerate(ir):
        # print(key, val[0],val[1],penst[myini],redundant[myini],"top")

        if myflag2 ==0 and redundant[myini] == 'r' and penst[myini] == "u" and (val[0].direction == 'forward' or val[0].direction == 'backward'):
                myflag2=1
                left = kachuaAST.Var(":__mtemp")
                right = kachuaAST.Num(0)
                intr = kachuaAST.AssignmentCommand(left,right)
                irgen.addInstruction(ir,intr,key-1)
                # print("control1")
                print(ir[0][0])
                # myini +=1
        
                       
        elif (isinstance(val[0], kachuaAST.MoveCommand)) and redundant[myini] == 'r' and penst[myini] == "u" and (val[0].direction == 'forward' or val[0].direction == 'backward'):
            
            # print("control2")
            if val[0].direction == 'forward':
                inby = val[0].expr
                left = kachuaAST.Var(":__mtemp")
                right = kachuaAST.Sum(kachuaAST.Var(":__mtemp"),inby)
                val = list(val)
                val[0] = kachuaAST.AssignmentCommand(left,right)
               
                myini += 1
        
            elif val[0].direction == 'backward' :
                dcby = val[0].expr
                left = kachuaAST.Var(":__mtemp")
                right = kachuaAST.Diff(kachuaAST.Var(":__mtemp"),dcby)
                val = list(val)
                val[0] = kachuaAST.AssignmentCommand(left,right)
                
                myini += 1
        elif (isinstance(val[0], kachuaAST.MoveCommand)) and redundant[myini] == 'n' and myflag2 == 1 and penst[myini] == 'u' and (val[0].direction == 'forward' or val[0].direction == 'backward'):
            # print("control3")
            if (val[0].direction == 'forward'):
                    mdby = val[0].expr
                    # left = kachuaAST.Var(":__mtemp")
                    val[0].expr = kachuaAST.Sum(kachuaAST.Var(":__mtemp"),mdby)
                    # val = list(val)
                    #  = right
            if val[0].direction == 'backward':
                    mdby = val[0].expr
                    val[0].expr = kachuaAST.Sum(kachuaAST.Var(":__mtemp"),mdby)
            myini +=1
        else:
            myini += 1
                        
            
        # print(myi,"mk",myini)   
        # print(myini-1)         
        # print(myini,"hello")
        if myi == myini:
            pass
            # print("contro")
            
        else: 
            print(val[0])
            # print(key,myini, val[0],val[1],penst[myini-1],redundant[myini-1])

        myi = myini
        



    return ir2


def genCFG(ir):
    # your code here
    
    #Finding leader
    lead = []
   
    for  key, item in enumerate(ir):

        # print(key,"xyz",item,type(item[1][2]))
        
        # print(item[1])
        if item[1] != 1:
            
            temp = key+item[1]
            lead.append(temp)
            lead.append(key+1)

    lead = list(set(lead))
    lead.sort()
    # print(lead)
    

  
    #Add a length of the ir at the end of the lead list (here below code demand it)
    lead.append(len(ir))

    
    #define the datastructure which will be passed in return of this function      
    myds =[]


    #define the initializers ld,i for the lead and ir respectively
    ld = 0
    i=0
    k = 0


    #Seperating the Blocks 
    while ld < len(lead):
        blk = []
        while i < len(ir):
                  
            if i < lead[ld]:
                blk.append((k , ir[i][0],ir[i][1]))
                k += 1
                i += 1
                #inblk += 1
           
            else:
                break
       
        myds.append(blk)
        ld += 1
    
    cfg = myds
    #print(cfg)
    

    return cfg
   
    

def dumpCFG(cfg):
    # dump CFG to a dot file
    
    #Finding the edges of the Control Flow Graph
    jmpedges = []
    for i in range(len(cfg)):
        for j in range(len(cfg[i])):
            if cfg[i][j][2] !=1:
                jmpedges.append((cfg[i][j][0],cfg[i][j][0]+cfg[i][j][2]))
               
    jmpedges = list(set(jmpedges))

    for i in range(len(jmpedges)):
        jmpedges[i]= list(jmpedges[i])
    #print(type(jmpedges[0]))

    
    for i in range(len(cfg)):
        for j in range(len(cfg[i])):
            for k in range(len(jmpedges)):
                if cfg[i][j][0] == jmpedges[k][0]:
                    jmpedges[k][0] = i
                if cfg[i][j][0] == jmpedges[k][1]:
                    jmpedges[k][1] = i
    
    
    
    # for i in range(len(jmpedges)):    
    #     print(jmpedges[i][0],jmpedges[i][1])                

    for i in range(len(jmpedges)):
        jmpedges[i]= tuple(jmpedges[i])

    edges = jmpedges
    # print("new",edges)

    for i in range(len(cfg)):

        edges.append((i,i+1))

    for i in range(len(cfg)):
        for j in range(len(cfg[i])):
            # print(cfg[i][j][1])
            # x= str(cfg[i][j][1])
            # print(x)
            if str(cfg[i][j][1]) == "False" :
                edges.remove((i,i+1))
                
                   
    
    edges = list(set(edges))
    edges.sort()
    # print(edges)


    #print(edges)

    print("\n========== Control Flow Graph Of the Given IR is==========\n")
    #Import graph for priting the Control Flow Graph
    import graphviz
    dot = graphviz.Digraph(comment='')
    dot  #doctest: +ELLIPSIS <graphviz.dot.Digraph object at 0x...>

    #Printing the Nodes
    for i in range(len(cfg)):
        m = []
        for j in range(len(cfg[i])):
            m.append(str(cfg[i][j][1]))
            print(str(m))

        dot.node(str(i), "\n".join(m))

    
    #Printing the Corresponding Edges
    for i in range(len(edges)):
        print(edges[i][1],"mani")
        if edges[i][1] >= len(cfg):
            dot.node("exit", "")
            dot.edge(str(edges[i][0]),"exit")
        else:
            dot.edge(str(edges[i][0]),str(edges[i][1])) 
    
    
    print(dot.source)  # doctest: +NORMALIZE_WHITESPACE
    dot.render('testcases/output1.txt', view=True)  # doctest: +SKIP 'testcases/output1.pdf'
      
    pass


