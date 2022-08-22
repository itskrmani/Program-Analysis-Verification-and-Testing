pendown
if :x > 0 [
	if :y > 0 [
		if :z > 0[

			forward :move
			right 10
		
		] else [backward 10]
		
	] else [backward 10]

	:move = :move + 10

] else [backward 10]