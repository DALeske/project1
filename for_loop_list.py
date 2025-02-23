# copy 5 times

text = "I will lsten to my teacher and complete my work on time"
for x in range (1,6):
    print(x,"-",text)

# count by 5 from 0 to 100
for i in range(0,101,5):
    print (i)

# Count down from 10 to 0
for j in range (0,11,1):
    print (10-j)

# Times table for 12
for k in range (0,11):
    print (k,"X 12 =",12*k)    

# cap letters A - Z
for g in range(65,91):
    print(chr(g))

# iterative sum
num = int(input("Enter a number:"))
sumt = 0
for y in range(1,num+1):
    sumt = (sumt + y)
print("Iterative Sum for",num," = " + str(sumt))