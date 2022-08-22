
	creator : Manish Kumar
	Roll no : 21111037
	
	
	To Run This Program Module:
		Make sure you are in the "assignment_1_21111037" folder
		to run the shell script use the command below
			sh run.sh <path-to-file>
			e.g. sh run.sh ./testcases/testcase1.py
		In case you are see "python3 not found" error, use run-python.sh
			sh run-python.sh <path-to-file>
			e.g. sh run-python.sh ./testcases/testcase1.py
			
	
	About This Program Module :
	
	this program module take python file as input and give their Assignment statement, 
	Branch and loop Conditions as output.
	    to create this module i used python language, and inside it i used number of 
	functions which are:
		def operator(x): takes string as input and return corresponding operator sign
		def condition(x): takes string condition as input and return corresponding 
						condition sign
		def Findtypec(info): takes list as input and find the value of type key
		def Findtypeo(info): takes list as input and find type of operator key in it
		def Findtype(info): takes list as input and if type key is 'For' , 'While' 
						then return it
		def Myfindtype(info): takes list as input and if type key is 'Name' , 'BinOp'
						'Expr' and 'AugAssign' then return it
		def Findvalue(info): takes list as input and return value field
		def Findid(info): takes list as input and return id
		def Findop(info): takes list as input and return id
		def Myfor( body, iter, orelse, target): to handle if 'For' loop come
		def Myinfor(body, orelse, test): to handle if 'For' loop comes inside any
						other loop or 'If' condition
		def Myassign(targets,value): to handle if Assignment statement come
		def Myinassign(body,orelse): to hanlde if Assignment statement comes inside any
						other loop or 'If' condition
		def Myaugassign(op, target, value): to handle if Augmented Assignment Statement comes
		def Mybranch(orelse, test): to handle 'If' conditions
		def Inbranch(test): to handle if 'If' comes comes inside any other loop or 'If' condition
		def Mywhile(body,orelse,test): to handle 'While' loop
		         rest statements are used to call these functions
				 
	
	


	
		