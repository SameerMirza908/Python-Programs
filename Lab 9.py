"""
a = input('Enter subjects :')
b = input('Enter subjects :')
c = input('Enter subjects :')
m1 = int(input('Enter marks :'))
m2 = int(input('Enter marks :'))
m3 = int(input('Enter marks :'))
  
dic = {a:m1,b:m2,c:m3}
print(dic)
  
  

duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(list(set(duplicate)))
mytuble = (list(set(duplicate)))
print("Maximum Value " , max(mytuble))
print("Minimum Value " , min(mytuble))



a = input("Enter a  month name :")

print("This month has days :",dic[a])


dic = {'January ': 31 , 'February': 28, 'March': 31 , 'April': 30,
       'May' : 31 , 'June': 30,'July':31,'Augest':31, 'September': 30,'October':31,
       'November':30,'December':31}


for i in dic:
    
     if dic[i] == 31:
         print(i)


dic = {'Sameer':22, 'Talha':21,'Faisal':15}

a = input('Enter Student name')

print("The age of student is :", dic[a])

dic1 = {}
a = True
while a:
     key = input("Enter a products :")
     value = int(input("Enter prices :"))
     dic1[key] = [value]
     b = input("Want to enter more products :(Yes/NO)")
     if b =="Yes":
         continue
     else:
         a = False
         
         
dollar = int(input("Enter a amount in dollar  $:"))
dollar = dollar * 197

print(dollar)
"""




    


a = [1,234,43443,2]

for i in a:
   # print(i)
    a.sort()
    print(i)

   
    
    

    


   

     

