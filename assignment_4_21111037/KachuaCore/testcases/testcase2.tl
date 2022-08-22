pendown
if (:x + :y > 50) [
    forward 20
    backward 30
] else [
    if (:x + :y < 30) [
        backward 100
    ]
    forward 100
]
penup