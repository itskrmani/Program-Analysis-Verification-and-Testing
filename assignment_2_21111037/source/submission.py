
import sys
sys.path.insert(0, './ast')

import kachuaAST

def genCFG(ir):
    # your code here

    
    #Finding leader
    lead = []
    for  key, item in enumerate(ir):
        if item[1] != 1:
            lead.append(key+item[1])
            lead.append(key+1)
               
    lead = list(set(lead))
    print(lead)
    
  
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
    
    
    
    for i in range(len(jmpedges)):    
        print(jmpedges[i][0],jmpedges[i][1])                

    for i in range(len(jmpedges)):
        jmpedges[i]= tuple(jmpedges[i])

    edges = jmpedges


    for i in range(len(cfg)-2):
        edges.append((i,i+1))
    
    edges = list(set(edges))


    #print(edges)

    print("\n========== Control Flow Graph Of the Given IR is==========\n")
    #Import graph for priting the Control Flow Graph
    import graphviz
    dot = graphviz.Digraph(comment='')
    dot  #doctest: +ELLIPSIS <graphviz.dot.Digraph object at 0x...>

    
    dot.node("exit", "")


    #Printing the Nodes
    for i in range(len(cfg)-1):
        m = []
        for j in range(len(cfg[i])):
            m.append(str(cfg[i][j][1]))
            #print(str(m))

        dot.node(str(i), "\n".join(m))

        
    #Printing the Corresponding Edges
    for i in range(len(edges)):
        if edges[i][1] >= len(cfg):
            dot.edge(str(edges[i][0]),"exit")
        else:
            dot.edge(str(edges[i][0]),str(edges[i][1])) 
    
    
    print(dot.source)  # doctest: +NORMALIZE_WHITESPACE
    dot.render('testcases/output.txt', view=True)  # doctest: +SKIP 'testcases/output.pdf'
    
    pass


