pendown
:x=40
:z=50
:y1 = :x + 20
if (:y1 > 42) [
  :y2 = :z - 20
  :t = :y1 + :y2
  forward :t
] else [
  :y2 = :w - 20
  :t = :y1 + :y2
  forward :t
]