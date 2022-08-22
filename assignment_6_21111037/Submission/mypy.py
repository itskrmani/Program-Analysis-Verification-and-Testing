import numpy as np
# mycol = 7
# activity_mat = [[1,1,1,1,0,0,1],[1,1,1,1,0,0,1],[1,1,1,1,0,0,0],[0,0,0,0,1,1,1]]
# activity_mat = np.array(activity_mat)

# mydict = {}
# indy = 0
# for i in range(mycol):
#     x = list(activity_mat[:, i])

#     mydict.update({indy:x})
#     indy= indy + 1


# print(mydict)
# print(activity_mat)
# indy2 = 0        
# w = np.zeros(mycol)

# for k in range(mycol):
#     for i in range(mycol):
#         if mydict.get(k) == list(activity_mat[:, i]):
#             w[k] = w[k] + 1

# w = w-1
# print(w)
# w = w /(mycol-1)
# sum = np.sum(w)
# ulysis = sum / mycol
# print(w,sum,ulysis)

####################################################################
def suspiciousness(icol,errvec):
    # icol = [1,1,1,1]
    # errvec = [1,1,1,0]
    Cp = Cf = Np = Nf =0
    for i in range(len(icol)):
        if icol[i] == 1 and errvec[i] == 0:
            Cp = Cp + 1
        if icol[i] == errvec[i] == 1:
            Cf = Cf + 1
        if icol[i] == errvec[i] == 0:
            Np = Np + 1
        if icol[i] == 0 and errvec[i] == 1:
            Nf = Nf + 1

    # print(Cp,Cf,Np,Nf)
    #Ochiai score
    # sus = Cf / np.sqrt((Cf + Nf)*(Cf + Cp))
    #Tarantula score
    try:
        sus_s = (Cf / (Cf+Nf))/((Cf / (Cf+Nf))*(Cp/(Cp+Np)))
    except ZeroDivisionError:
        sus_s = 0

    # sus_s = (Cf / (Cf+Nf))/((Cf / (Cf+Nf))*(Cp/(Cp+Np)))


    # print(sus)
    return sus_s


######################################################################

sus = []
col = 2

# suspicious call

m = []

m.insert(0, "c"+ str(0)) 
m.insert(1, suspiciousness([1,0,1,1], [1,1,1,0])) 
sus.insert(0,m)

m = []

m.insert(0, "c"+ str(1)) 
m.insert(1, suspiciousness([1,1,1,1], [1,1,1,0])) 
sus.insert(1,m)

m = []

m.insert(0, "c"+ str(2)) 
m.insert(1, suspiciousness([1,1,0,0], [1,1,1,0])) 
sus.insert(2,m)


print(sus)

import sys
max = -sys.maxsize
# print(max)
rankList = []

for k in range(3):
    for i in range(len(sus)):
        if max <= sus[i][1]:
            max = sus[i][1]
            mark = i
    print(mark,max)
    
    rankList.insert(k, [sus[mark][0],k ])
    sus.remove(sus[mark]) 
    max = -sys.maxsize
    print(sus)
    
    print(rankList,"ranklist", sus,"sus")

    
    
