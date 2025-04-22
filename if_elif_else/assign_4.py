#assignment - 4

temperature = float(input("enter the temperature in °C:"))
is_raining = input("is_raining:(yes/no)")

if temperature>30:
    if is_raining == "yes":
        print(" stay indoors and watch a movie")
    else:
        print("Go Swimming")

elif 20 < temperature  <=30:
    if is_raining == "yes":
        print("visit a museum")
    else:
        print("perfect for a picnic")
        
elif 10 < temperature  <=20:
    if is_raining == "yes":
        print("indoor sports recommended")
    else:
        print("Go for a walk")

else:
    if is_raining == "yes":
        print("stay home with hot chocolate")
    else:
        print("ice skating would be fun")

