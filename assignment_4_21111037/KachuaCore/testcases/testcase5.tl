pendown

repeat 3[
if (:x + :y > 45) [
    forward 20
    backward 30
] 
if (:x + :y < 30) [
        backward 100
]
if(:x < 2000)[
	forward 20
]
if(:y > 350)[
	backward 30
]else [
	forward 40
	backward 36

]]
penup