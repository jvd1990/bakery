# bakery
bakerydict = {
    "barbari" : 2,
    "taftoon" : 1,
    "sangak" : 3,
    "lavash" : 1,
    "baget" : 2
}
# name
name = input("what is your name: ")
# Password
password = int(input(f"please choose your pasword {name}: "))
#login
login = int(input(f"please enter your pasword {name}: "))
while login != password:
    print("The password entered is incorrect.please try again. ")
    login = int(input(f"please enter your pasword {name}: "))
    if login == password:
        print("The password is correct.")
#bread
total_cost = 0
print("barbari = 2 $ taftoon = 1 $ sangak= 3 $ lavash=1 $ baget= 2")
bread = input(f"which kind of bread do you want {name}: ")

if bread in bakerydict:
    number = int(input(f"how many {bread} do you want {name}: "))
    total_cost += bakerydict[bread] * number

order = input(f"do you want another bread (yes/no)? ")

while order == "yes":
    bread = input(f"which kind of bread do you want {name}: ")
    if bread in bakerydict:
        number = int(input(f"how many {bread} do you want {name}: "))
        total_cost += bakerydict[bread] * number
    order = input(f"do you want another bread (yes/no)? ")

print(f"ok, I will prepare now. The total cost is {total_cost} dollars.")