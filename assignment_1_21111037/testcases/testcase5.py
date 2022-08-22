# testcase_5 Program to display the Fibonacci sequence up to n-th term

nterms = 10

# first two terms
n1 = 0
n2 = 1


if nterms <= 0:
   print("Please enter a positive integer")

elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)

else:
   for count in range(1, nterms):
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
