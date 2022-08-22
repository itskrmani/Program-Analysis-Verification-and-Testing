    This module uses Kachua 3.2 version

    Limitation:
     This Module work for Equal case only for ex: c1 + 20 = 40 

    To run this module: 
        Module is taking two programs written by user and it tell whether they are 
    equivalent to each other or not,if equal then find the constraints for which they are euqal.

    so first take Program1 and make sure your are in KachuaCore Folder and then run ==>
    In windows  :
        python ./kachua.py -t 100 -se testcases/eqtest1.tl -d "{':x': 40, ':y': 100}" -c "{':c1':1,':c2':1}"

        where eqtest1.tl contain Program1 and -d flag used here to seed inputs (here :x take 40,:y take 100 value), 
        and -c flag used here to give initial values to the constraint (shown inside the Program1)
        

    now we require a .kw file for that we run command ==>
        python kachua.py -O testcases/eqtest2.tl
        which generate a optimized.kw file inside KachuaCore folder which then move to Submission folder

    Now for Program2 make sure you are in Submission folder to run this query.
        python symbSubmission.py -b optimized.kw -e "['x', 'y']" 

        if solver generate "sat", then module will generate the constraints for which both the programs are equal(provided programs
        are equivalent to each other.)


    
    Inside this Module:
        I implemented the eqcheck() method and interpret() method ==>

        interpret() : take ir, testData[indx]['params'] as a input and return the interpreter.ConcreteInterpreter object.
         
         ir == > Intermediate Representation.
         testData[indx]['params'] ==> Parameters value which contain inside testdata file.
         

        eqcheck() : take args,ir as a input and return output whether both program are equal or not, if equal then return value of the constraint
        c1, c2 for which both the programs are equals or not.

         inside the funtion : 
            
            First load the testData.json file as a read mode then convert its type in 'dict' type from 'str'
            
            close the file
            
            initiate the z3solver() instance
            
            Iterate the testData dictionary
            
            fetch 'params' and 'symbEnc' value
            
            Iterate the 'params' value to add all the symbolic variable m to solver
            
            Iterate val list and then inside iterate the args.output (user feeded values) 
            
            and Replace all the args seeded from the user with their corresponding Symbolic value
            
            then Equate the user seeded value with their corresponding value that already we have in myptr.prg
            
            Check if solver return "sat" , if it is that means solution to the entered equation have exists