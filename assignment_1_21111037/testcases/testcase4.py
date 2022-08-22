# testcase_4 Program to check if a number is prime or not

num = 29


flag = False

# prime numbers are greater than 1
if num > 1:
    
    for i in range(2, num):
        if num % i == 0:
            
            flag = True
           
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
	
	