# 1. initialize the total to 0
# 2. loop through all the numbers adding each number to the total
# 3. divide the total by the number of numbers to get the average
total = 0
numbers = 0
for line in open("scores.txt"):
    num = int(line)
    total = total + num
    numbers = numbers + 1

average = total / numbers
print(average)



#for i in range(20):
#    print(i)

