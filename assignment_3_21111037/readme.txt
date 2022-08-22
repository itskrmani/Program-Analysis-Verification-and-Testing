

 	code work only on Kachua-v2.0_4
	In IRgen plz import pickle
	from kast import kachuaAST
	and replace ir2 to ir in optimize return
	Limitation: does not work for if else statements

	
	to run the Module:
		python3 ./kachua.py -O example/test.tl

	About This Module:
		in this module three analysis are run:
		1) for PenStatus
		2) for Finding Redundant Move
		3) then Eliminate the Redundant Move

	1) for finding the penstatus i use forward analysis:
		find IN and OUT for the each basic block in forward analysis
		and the according to those IN and OUT finding the 
		status of pen.
		for penstatus i maintain a list which could contain,
		u: Penup
		d: Pendown
		IN, OUT contain the status of their predessor's and Successor's basic blocks.
		and if there condition of join come then i use the 'AND' between them.
			for ex:  u ^ u = u , u ^ d = d, d ^ u = d, d ^ d = d
		
			now we have a list of penstatus

		
	2) for finding the Redundant Move i use backward analysis:
		find IN and OUT for the each basic block in backward analysis
		and the according to those IN and OUT finding the 
		Redundant move statment.
		for redundant move i maintain a list which could contain,
		r: Redundant move
		n: Non-Redundant move
			here i maintain a flag to track the move which should not be updated to
		__mtemp expressions.
		IN, OUT contain the status of their predessor's and Successor's basic blocks.
		and if there condition of join come then i use the 'AND' between them.
			for ex: r ^ r = r, n ^ r = n, r ^ n = n, n ^ n = n
		
			now we have a list of redundant move marking

	3) now to remove the redundant move i use forward analysis:
		here i maintain a flag to track the first redundant move for which i have to add
		instruction(__temp=0).
		here we have two list i.e. penstatus list, redundant move list
		now i only update the statments if there status of pen is 'u' and status of 
		redundant move is 'r'
		final output is optmized Intermediate Instructions
			