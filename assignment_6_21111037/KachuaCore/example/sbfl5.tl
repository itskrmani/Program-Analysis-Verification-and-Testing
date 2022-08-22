pendown
if :x > 0 [
	if :y > 0 [
		if :z > 0 [
			forward 10
            left 45
            backward 10
            right 45
		]
		else [
            backward 10
            left 45
            forward 20          
            
            ]
	]
	else [
        backward 10
        left 45
        forward 20   
    ]
]
else [
    
    backward 10
    left 45
    forward 20   
]

if :x > 0 [
	if :y > 0 [
		if :z > 0[

			forward :move
			right 10
		
		] else [
            backward 10
            left 45
            forward 20   ]
		
	] else [
        backward 10
        left 45
        forward 20   
    ]


	:move = :move + 10

] else [backward 10]