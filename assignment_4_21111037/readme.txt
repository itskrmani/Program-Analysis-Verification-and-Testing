    This module use kachua-v2.3

    To Run this module:
    At Windows ==> 
        python ./kachua.py -t 50 --fuzz testcases/testcase4.tl -d "{':x' : 5,':y' : 100}" 

    At Linux ==>
        python ./kachua.py -t 50 --fuzz testcases/testcase4.tl -d '{":x" : 5,":y" : 10}' 

    
    Assumptions:
    Time budget for fuzzing in seconds which i took is 50 seconds to every testcase
    for testcase 1 ==> input variable taken :move = 10 
    for testcase 2 ==> input variable taken :x = 5 , :y = 100
    for testcase 3 ==> input variable taken :shapes = 11, :space = 50, :move = 5, :dir = 15
    for testcase 4 ==> input variable taken :x = 5 , :y = 100
    for testcase 5 ==> input variable taken :x = 5 , :y = 100
    for testcase 6 ==> input variable taken :vara = 5 , :varb = 25
    
    Limitation:
        Module is run and tested on windows machine
        It is possible that fuzzer not will cover all the statements (after all work on random values)

    About This Module:
        In the submission.py there are two classes i.e. CustomCoverageMetric, CustomMutator
        In CustomCoverageMetric we have two methods i.e. compareCoverage(), updateTotalCoverage()
            In compareCoverage() Method, just compare two list i.e. curr_metric, total_metric
        if any element of curr_metric is not in total_metric then just set the flag, and further if flag
        is set then return True (returning True depict that surely more number of statements are cover in curr_metric
        than previous statements)
            In updateTotalCoverage() Method, just union curr_metric and total_metric into total_metric, by making them set
        and then typecast to list and return total_metric

        In CustomMutator class there is a method named  mutate()
         mutate() method must be implement such that it take input and convert it into random input for that
        i create four function f1(),f2(),f3(),f4() which converts input value into random numbers as well as they are call
        randomly for each input.

        Method which flip single bit, f0() ==> take input_data.data[value] and convert into binary with the help of bin() function and then it
        further typecast into list.
                the output of bin(5) is like 0b101 , so here 0b should not be flip so just skip them for flipping
        process. In flipping simply check random index (should be 2 to len-1) and convert it into opposite bit.
                now we have bit flipped list which will converted into str form by ''.join(map()) function
                now convert string form into int and return input_data.data

        Method which flip two bits, f1() ==> take input_data.data[value] and convert into binary with the help of bin() function and then it
        further typecast into list.
                same process mention above till flip single bit, after that again calculate the random number and flip another index of list.
                now we have bit flipped list which will converted into str form by ''.join(map()) function
                now convert string form into int and return input_data.data

        Method which uses Arithmetic Technic, f2() ==> According to article https://lcamtuf.blogspot.com/2014/08/binary-fuzzing-strategies-what-works.html
        experimental choosen range is -35 to 35.
                so i generate the random number between -35 to 35 and ADD it to input_data.data[value] and return input_data.data
        
        Method which uses Interested inputs i.e. -1,0,1,MAX_INT,MIN_INT,MAX_INT-1,MIN_INT+1, f3()
                define a list of Intersted inputs, pick randomly and assign this to input_data.data[value]
                and return input_data.data