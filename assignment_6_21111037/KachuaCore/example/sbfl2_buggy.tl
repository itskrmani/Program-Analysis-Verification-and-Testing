pendown
if :x > 0 [
	if :y > 0 [
		if :z > 0[

			forward :move
			right 10
		
		] else [backward 10]
		
	] else [backward 15]

	:move = :move + 12

] else [backward 10]