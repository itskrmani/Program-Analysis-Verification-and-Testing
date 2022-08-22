pendown
:x=40
:z=50
:y1 = :x + 20
forward :y1
if (:y1 > 42) [
  :y2 = :z - 20
  forward :y2
] else [
  :y2 = :w - 20
  forward :y2
]