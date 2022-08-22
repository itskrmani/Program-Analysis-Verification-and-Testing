
import json
from ast import parse
from ast2json import ast2json
import sys

ast = ast2json(parse(open(sys.argv[1]).read()))
json_obj = ast['body']
 
def operator(x):
    if x=='Add':
        return ' + '
    if x=='Mult':
        return ' * '
    if x=='Div':
        return ' / '
    if x=='Mod':
        return ' % '
    if x=='Sub':
        return ' - '
    if x=='BitAnd':
        return ' & '
    if x=='BitOr':
        return ' | '
    if x=='BitNot':
        return ' ~ '
    if x=='BitXor':
        return ' ^ '
    if x=='LShift':
        return ' << '
    if x=='RShift':
        return ' >> '
    
    
def condition(x):
    if x=='Eq':
        return ' == '
    if x=='NotEq':
        return ' != '
    if x=='Lt':
        return ' < '
    if x=='LtE':
        return ' <= '
    if x=='Gt':
        return ' > '
    if x=='GtE':
        return ' >= '
    if x=='Is':
        return ' Is '
    if x=='IsNot':
        return ' IsNot '
    if x=='In':
        return ' In '
    if x=='NotIn':
        return ' NotIn '
    if x=='MatMult':
        return ' @= '
    

def Findtypec(info):
    for i in info:
        a=condition(i['_type'])
        return a

def Findtypeo(info):
    for i in info:
        a=operator(i['_type'])
        return a
    
def Findtype(info):
    for j in info:
        if j['_type']=='For':
            return 'For'
        if j['_type']=='While':
            return 'While'

def Myfindtype(info):
    for j in info:
        if j['_type']=='Name':
            return 'Name'
        if j['_type']=='BinOp':
            return 'BinOp'
        if j['_type']=='Expr':
            return 'Expr'
        if j['_type']=='AugAssign':
            return 'AugAssign'
        
        
def Findvalue(info):
    for i in info:
        a=i['value']
        return a
    
def Findid(info):
    if info['args'][1]['_type'] =='Name':
        x= info['args'][1]['id']
 
    else:
        x = info['args'][1]['left']['id']
        
    return x 
   
def Findop(info):
    if info['args'][1]['_type'] =='Name':
        x= info['args'][1]['id']
 
    else:
        x = info['args'][1]['left']['id']
        
    return x 
   
       
 
def Infor( iter,target):
    A=tuple()
    if iter['args'][1]['_type'] == 'Name':
        A = str(target['id']) + ' in ' + str(iter['func']['id']) + '(' + str(Findvalue(iter['args'])) + ',' + str(Findid(iter)) + ')'

    else:
        A = str(target['id']) + ' in ' + str(iter['func']['id']) + '(' + str(Findvalue(iter['args'])) + ',' + str(Findid(iter)) + operator(iter['args'][1]['op']['_type']) +  str(iter['args'][1]['right']['value'])+ ')'
    print(A)
    
       
def Myfor( body, iter, orelse, target):
    Infor( iter, target)
    for i in body:
        if i['_type'] == 'For':
           Myfor(i['body'], i['iter'], i['orelse'], i['target'])
           
        if i['_type'] == 'While':
            Mywhile(i['body'],i['orelse'],i['test'])
    
         
def Myinfor(body, orelse, test):
   # print(orelse)
    for i in orelse:
        
        if i['_type']=='If' :
            
            Myinfor(i['body'],i['orelse'],i['test'])
        if i['_type']=='Expr':
            return 0
            
        if i['_type']=='For':
            Myfor(i['body'],i['iter'],i['orelse'],i['target'])
        
        if i['_type']=='While':
            Mywhile(i['body'],i['orelse'],i['test'])
    
    for i in body:
        
        if i['_type']=='If' :
            
            Myinfor(i['orelse'],i['test'])
        if i['_type']=='Expr':
            return 0
            
        if i['_type']=='For':
            Myfor(i['body'],i['iter'],i['orelse'],i['target'])
        
        if i['_type']=='While':
            Mywhile(i['body'],i['orelse'],i['test'])
       
def Myinassign(body,orelse):
     
    for i in orelse:
        #print(i['body']['_type'])
        #print(i['body'])
        #x = str(orelse['_type'])
        if Myfindtype(orelse) != 'Expr':
            for k in i['body']:
            #if k['_type']=='Expr':
               # return 0
               if k['_type']=='AugAssign':
                Myaugassign(k['op'],k['target'],k['value'])
            
                     
          
        if i['_type']=='Assign':
            
            a=Myassign(i['targets'],i['value'])
            print(a)
        
        elif i['_type']=='If' or i['_type']=='For' or i['_type']=='While' :
            
            Myinassign(i['body'],i['orelse'])
        
        elif i['_type']=='Expr':
           for i in range(1,len(body)):
                
                if body[i]['_type']=='Assign':
                    #print(body[i]['value'])
                    a=Myassign(body[i]['targets'],body[i]['value'])
            
                    print(a)
            #return 0
    
    
    

    for i in body:
             
        if i['_type']=='If' or i['_type']=='For' or i['_type']=='While' :
            Myinassign(i['body'],i['orelse'])
                        
        elif i['_type']=='Assign':
            
            a=Myassign(i['targets'],i['value'])
            
            print(a)
            
        elif i['_type']=='Expr':
            for i in range(1,len(body)):
                
                if body[i]['_type']=='Assign':
                    #print(body[i]['value'])
                    a=Myassign(body[i]['targets'],body[i]['value'])
            
                    print(a)
            return 0
    
def Myassign(targets,value):
    A=tuple()
    
    if value['_type']=='Constant':
        m=str(value['value'])
        
    elif value['_type']=='BinOp':
        n,o=0,0
        for j in value['right']:
            if j=='value':   
                n=1
            if j=='id':
                o=1
        if n:
           m=str(value['left']['id'])+operator(value['op']['_type'])+str(value['right']['value'])
        if o:
           m=str(value['left']['id'])+operator(value['op']['_type'])+str(value['right']['id'])
    
    elif value['_type']=='Name':
        m= value['id']
        
            
    for i in targets:
        A=i['id']+" = "+m
    return A
 

def Myaugassign(op, target, value):
    A = tuple() 
    A = str(target['id']) + operator(op['_type']) + '= '  + str(value['value'])
    print(A)

 
def Inbranch(test):
    A=tuple()

    if test['_type'] == 'Name':
        A = test['id']
        
        #print(A)
        
    elif test['_type'] == 'Compare':
        #print(test)
        for j in test['comparators']:
            
            if j['_type']=='Constant' and test['left']['_type']=='Name':
                
                A=str(test['left']['id'])+str(Findtypec(test['ops']))+str(j['value']) 
                
            elif j['_type']=='Constant' and test['left']['_type']=='BinOp':
                                
                A=str(test['left']['left']['id']) + operator(test['left']['op']['_type']) + str(test['left']['right']['value'])  + str(Findtypec(test['ops']))+str(j['value']) 
                
            elif j['_type']=='Name':
                
                A = str(test['left']['id'])+str(Findtypec(test['ops'])) + str(j['id'])
                
            elif j['_type']=='BinOp':
                
                A = str(test['left']['id'])+str(Findtypec(test['ops'])) + str(j['left']['id']) + operator(j['op']['_type']) + str(j['right']['value'])
                
    
    print(A)
            



def Mybranch(orelse, test):
    Inbranch(test)
    #if not len(orelse):
        
    if Findtype(orelse)=='For' :
       
        return 0
    elif Myfindtype(orelse)=='Expr':
       
        return 0
    
    else :
          
        for j in orelse:
            #Inbranch(test)
            #print(orelse['_type'])
            Mybranch(j['orelse'],j['test'])
            




def Mywhile(body,orelse,test):
    if not len(orelse):
        Inbranch(test)
    else:
        for j in orelse:
            Inbranch(test)
            Mybranch(j['orelse'],j['test'])
 

    
        
    
          
        
print('\n')
  
print("Assignment Statements:")
for i in json_obj:
    if i['_type']=='Assign' :
        a = Myassign(i['targets'],i['value'])
        print(a)
    if i['_type']=='AugAssign':
        Myaugassign(i['op'],i['target'],i['value'])
        
        #A+=a
for i in json_obj:
    if i['_type']=='While' or i['_type']=='For' or i['_type']=='If' :
        Myinassign(i['body'],i['orelse'])
    
       


print('\n')

        
  
print("Branch Conditions:")
for i in json_obj:
    if i['_type']=='If':
         Mybranch(i['orelse'],i['test'])


print('\n')
         
         
         
print("Loop Conditions:")
for i in json_obj:
    if i['_type']=='While':
         Mywhile(i['body'],i['orelse'],i['test'])
for i in json_obj:
    if i['_type']=='For':
        Myfor(i['body'],i['iter'],i['orelse'],i['target']) 
for i in json_obj:
    if i['_type']=='If':
         Myinfor(i['body'],i['orelse'],i['test'])

      
         
        






