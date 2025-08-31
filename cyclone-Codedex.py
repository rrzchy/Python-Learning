
height = int(input("y? "))
credits = int(input("money? "))

def cyc(x, y):
  if height >= 137 and credits >= 10:
    print("Enjoy the ride")
  elif height <= 137 and credits >= 10:
    print("You are not tall enough to ride.")
  elif height >= 137 and credits <= 10:
    print("You dont't have enough credits")
  else:
    print("No req met")

cyc(height, credits)