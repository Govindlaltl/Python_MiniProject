print("WELCOME TO THE TIP CALCULATOR")
bill=float(input("What was the total bill ? "))
tip=int(input("How much tip would you like tto give? 10,20,30 ? "))
split=int(input("How manny people to split the bill ? "))
amount=(bill+tip)/split
print("Each person should pay: ",amount)