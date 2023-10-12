# 1
print("1.")
Name = input("Hello, what is your name?: ")
print ("Hello, "+str(Name)+". Good to meet you!")
print()

#2
print("2.")
Celsius = float(input("Enter a Celsius Temprature: "))
Fahrenheit = round((Celsius * 9/5) + 32, 2)
print(Celsius,"°C is equivalent to",Fahrenheit,"°F")
print()

#3
print("3.")
Students = int(input("How many students?: "))
GroupS = int(input("Required group size?: "))
Div = (Students//GroupS)
Mod = (Students%GroupS)
if Mod == 1:
    print("There will be", Div, "groups with", Mod, "student left over")
else:
    print("There will be",Div,"groups with",Mod,"students left over")
print()

#4
print("4.")
Pupils = int(input("How many pupils?: "))
Sweets = int(input("How many sweets?: "))
Div = (Sweets//Pupils)
Mod = (Sweets%Pupils)
if Mod == 1:
    print("Each student will get", Div, "sweets with", Mod, "sweet left over")
else:
    print("Each student will get", Div, "sweets with", Mod, "sweets left over")
print()



