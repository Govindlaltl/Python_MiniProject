import random
print(""" 
    ____   _    ____ ______        _____  ____  ____        
    |  _ \ / \  / ___/ ___\ \      / / _ \|  _ \|  _ \       
    | |_) / _ \ \___ \___ \\ \ /\ / / | | | |_) | | | |      
    |  __/ ___ \ ___) |__) |\ V  V /| |_| |  _ <| |_| |      
    |_|_/_/___\_\____/____/_ \_/\_/  \___/|_|_\_\____/___  _ 
    / ___| ____| \ | | ____|  _ \    / \|_   _/ _ \|  _ \| |
    | |  _|  _| |  \| |  _| | |_) |  / _ \ | || | | | |_) | |
    | |_| | |___| |\  | |___|  _ <  / ___ \| || |_| |  _ <|_|
    \____|_____|_| \_|_____|_| \_\/_/   \_\_| \___/|_| \_(_)""")
letter=int(input("Number of letters: "))
symbol=int(input("Number of symbols: "))
number=int(input("Number of numbers: "))
password=[]
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symb=['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',';',':',',','.','<','>','?','/','/']
num=['0','1','2','3','4','5','6','7','8','9']
for i in range(1,letter+1):
    rand=random.choice(alphabet)
    password+=rand
for i in range(1,symbol+1):
    password+=random.choice(symb)
for i in range(1,number+1):
    password+=random.choice(num)
random.shuffle(password)
new_password=''
for i in password:
    new_password+=i
print("The password is: ",new_password)