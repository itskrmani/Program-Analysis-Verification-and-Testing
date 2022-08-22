# testcase_6  Nested loop sequence

count = 0
while count < 3:   
    count = count + 1
    print("hello iitk")


num= 4
for i in range(1, num):
    while num > 0:
        print(num)
        num = num - 1
    for i in range(2, num):
        while count < 3: 
            count = count + 1
            print("hello iitk")
        for i in range(3, num):
            print(i)
