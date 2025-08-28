a = 0
b = 1

n= int(input("What is n? \n"))

# print(a)
# print(b)

for i in range(n):
   if i == 0:
      print(a)
   elif i == 1:
      print(b)
   else:
        c = a + b
        a = b 
        b = c
        print(c)
