# Nested if / else
# if condition:
#   if another condition:
#     do this
#   else:
#     do this
# else: 
#   do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5.0")
  elif age <= 18:
    print("Please pay $7.0")
  # elif age < 22:

  # elif
  # elif
  else:
    print("Please pay $12.0")
else:
  print("Sorry, you have to be this tall!")