pendown
if :x > 0 [
	if :y > 0 [
		if :z > 0 [
            left 45
			forward 10
            right 45
            backward 10
		]
		else [
            backward 10
            left 45
            forward 10
            right 45
            ]
	]
	else [ 
        backward 10
        left 45
        forward 100
        right 45]
]
else [ 
    backward 10
    left 45
    forward 80
    right 45 ]
