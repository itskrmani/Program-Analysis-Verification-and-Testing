
repeat 2 [
:varc = 10
if (:varc == 0) && (:vara < :varb) [
   forward 40
   backward 55
]

if :varc != 0 && (:vara < :varb) [
   forward 40
   backward 35
]

if :vara < :varb || :vara == :varb [
   forward 40
   backward 35
]]

