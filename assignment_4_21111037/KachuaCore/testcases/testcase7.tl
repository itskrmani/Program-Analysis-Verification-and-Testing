:y1 = :x1 + 20

if (:y1 > 42) [
  :y2 = :z - 20
  forward 100
  

  if (:y1 > 12) [
    :y2 = :z - 20
    :x1 = :z - 30
    :x1 = :z - 30
    backward 100
  
    if :y1 < :y2 [ 
      :y1 = 10  
      forward 120
      backward 200
      ]
  ]
  else [
  
   forward 90
 

  ]
  
] else [
  :y2 = :w - 20
  :y1 = :x1 + 20
]

:y1 = :y1 + 20

