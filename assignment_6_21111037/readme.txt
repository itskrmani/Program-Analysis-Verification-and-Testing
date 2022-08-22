
i am refering this article for suspiciousness function
https://www.sciencedirect.com/science/article/abs/pii/S0950584921000021

    Limitation:
        This module will run on Kachua-v5.0
        Created and Tested on Windows only
        it is possible that some time SBFL does not give correct order or ranking

    To Run this Module:
    Make Sure you are inside the  C:\...\Kachua-v5.0\KachuaCore> folder
      
      then in windows run this module by command : 

        to run case 1:
        python kachua.py --SBFL ./example/sbfl1.tl --buggy ./example/sbfl1_buggy.tl -vars "[':x', ':y', ':z']" --timeout 40 --ntests 20 
        --popsize 100 --cxpb 1.0 --mutpb 1.0 --ngen 100 --verbose True

        to run case 2:
        python kachua.py --SBFL ./example/sbfl2.tl --buggy ./example/sbfl2_buggy.tl -vars "[':x', ':y', ':z',':move']" --timeout 
40 --ntests 20 --popsize 100 --cxpb 1.0 --mutpb 1.0 --ngen 100 --verbose True >output2.txt

        to run case 3:
        python kachua.py --SBFL ./example/sbfl3.tl --buggy ./example/sbfl3_buggy.tl -vars "[':x', ':y', ':z',':a',':b',':c']" --timeout 
        40 --ntests 20 >output3.txt

        to run case 4:
        python kachua.py --SBFL ./example/sbfl4.tl --buggy ./example/sbfl4_buggy.tl -vars "[':vara', ':varb', ':varc']" --timeout 
        40 --ntests 20 --popsize 100 --cxpb 1.0 --mutpb 1.0 --ngen 100 --verbose True >output4.txt

        to run case 5:
        python kachua.py --SBFL ./example/sbfl5.tl --buggy ./example/sbfl5_buggy.tl -vars "[':x', ':y',':z', ':move']" --timeout 
        40 --ntests 20 --popsize 100 --cxpb 1.0 --mutpb 1.0 --ngen 100 --verbose True >output5.txt


    About this Module:

    In this i implemented three functions in sbflSubmission.py which are fitnessScore, suspiciousness, getRankList

    fitnessScore: for this function there is Activity_mat (matrix) is given by which i created a dictionary which contain columnwise 
    data of activity_mat matrix.
    by which i check for each column for its duplicacy.
    then apply ulysis score and finding the fitness which is return in float data.

    suspiciousness: for this function i refer above mentioned paper in which number of formulas are given for finding suspiciousness,
    but i found Tarantula score good for our given limited testsuite inputs. so i use that, however in the sbflSubmission file there
    are all the Score formulas are implemented(Commented)
     for that i calculate the 
                    Cp,Cf,Np,Nf
        Cf = Number of failing tests that execute C
        Cp = Number of passing tests that execute C
        Nf = Number of failing tests that do not execute C
        Np = Number of passing tests that do not execute C
         
        with that formulas are implemented
    
    getRankList: for this function we have to order the columns components according to there rank(max suspiciousness rank high), and return 
    it into given format i.e. 
        rankList will contain data in this format:
            suppose c1,c2,c3,c4 are components and their ranks are
            1,2,3,4 then rankList will be :
                    [[c1,1],
                     [c2,2],
                     [c3,3],
                     [c4,4]]
