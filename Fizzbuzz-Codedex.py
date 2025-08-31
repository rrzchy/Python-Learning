
n = int(input("Num"))

def fizzbuzz(n):
    for i in range(n):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 15 == 0:
            print("Fizzbuzz")
        else:
            print(i)

fizzbuzz(n)