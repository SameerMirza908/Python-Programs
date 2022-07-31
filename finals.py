
"""

li = [30,60,90]

number = li[0] 
for i in li:
     if i < number:
        number = i
        
print(number)


l = [5,5,5,9,5,5,5]

num = 0

for i in l:
    if i == 5:
        num = num + 1
print(num)


def convert(li):
    print(list(li))
 
l = ('Faisal', 'Ssacs')
convert(li)

dic = {'Maths':80, 'Physics':70}

a = input('Enter the subject :')
print(dic[a])
t = (3,7,3,7)

print(t[3])


a = eval(input("How much higher you want to print the triangle ?: "))
for i in range(0,a,1):
        print('*'*(i))
        


    
height = 5

def printS() :
    for i in range(0,height) :
        for j in range(0,height) :
            if ( (i == 0 or i == height // 2 or i == height - 1) ):
                print("*",end="")
            elif ( i < height // 2 and j == 0 ) :
                print("*",end="")
            elif ( i > height // 2 and j == height - 1 ) :
                print("*",end="")
            else :
                print(end=" ")
        print()
        
printS()

"""

a = [9,3,2,2,34]
l=a
print(l)

 
    
 


































