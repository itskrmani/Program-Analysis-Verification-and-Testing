

	To Run This Module:
		Make sure to put the submission.py file into kachua module.
		Make sure you are the folder which contain kachua.py, 
		submisson.py and .gitignore files and ast, parser and testcase 
		folder
 			example in my case "root@PC-name:~/assignment_2_21111037#"

		then just write the command in the terminal
				python3 ./kachua.py ./testcases/testcase1.tl

		if python3 is not supported then just type
				python ./kachua.py ./testcases/testcase1.tl



	About This Module:
		this module take input as a Intermediate Represenatation and
	convert that into Control Flow Graph into a pdf Which can be easily 
	seeable.
		In this module(Submission.py) has two function genCFG(ir)
	and dumpCFG(cfg).
		genCFG(ir), taking ir as a input and make a datastrcture of 
	of the given Basic Blocks, and then First find the Leader and then 
	according to that Blocks are being seperated.
		dumpCFG(cfg), taking Basic Blocks datastructure as a input
	and convert that into visual Control Flow Graph in pdf format. 
 