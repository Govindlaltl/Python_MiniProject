print(""" 
  ____    _    _     ____ _   _ _        _  _____ ___  ____  _ 
 / ___|  / \  | |   / ___| | | | |      / \|_   _/ _ \|  _ \| |
| |     / _ \ | |  | |   | | | | |     / _ \ | || | | | |_) | |
| |___ / ___ \| |__| |___| |_| | |___ / ___ \| || |_| |  _ <|_|
 \____/_/   \_\_____\____|\___/|_____/_/   \_\_| \___/|_| \_(_)""")


a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
print("""
1)Addition
2)Subtraction
3)Multiplication
4)Division""")
choice=int(input("Enter ur choice: "))
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:
    print(a*b)
elif choice==4:
    if b==0:
        print("Not possible!")
    else:
        print(a/b)