

Gryff = 0
Raven = 0
Huffy = 0
Slyth = 0

sc_1 = int(input("Q1) Do you like Dawn or Dusk? \n1) Dawn \n2) Dusk \n"))
if sc_1 == 1:
    Gryff += 2
    Raven += 2
elif sc_1 == 2: 
    Huffy += 2
    Slyth += 2
else:
    print("wrong input")

sc_2 = int(input("Q2) When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n"))

if sc_2 == 1:
    Huffy += 2
elif sc_2 == 2: 
    Slyth += 2
elif sc_2 == 3: 
    Raven += 2
elif sc_2 == 4: 
    Gryff += 2
else:
    print("wrong input")

sc_3 = int(input("Q3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n"))

if sc_3 == 1:
    Slyth += 4
elif sc_3 == 2: 
    Huffy += 4
elif sc_3 == 3: 
    Raven += 4
elif sc_3 == 4: 
    Gryff += 4
else:
    print("wrong input")

print(Gryff, Huffy, Raven, Slyth)

maxi = max(Gryff, Huffy, Raven, Slyth)

if Gryff == maxi:
    print("Gryff")
elif Huffy == maxi:
    print("Huffy")
elif Raven == maxi:
    print("Raven")
else:
    print("Slyth")