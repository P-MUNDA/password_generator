import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


####### easy methode#######

passward=''
for lr in range(1,nr_letters+1):
    passward+= random.choice(letters)
    print(passward)

for sy in range(1,nr_symbols+1):
    passward+=random.choice(symbols)
    print(passward)
for nu in range(1,nr_numbers):
    passward+=random.choice(numbers)
    print(passward)
print(f'Your passward is : {passward}')


####my hard methode ######

hardpass=''
passleng=len(passward)
for ss in range(1,passleng+1):
    hardpass+=random.choice(passward)
    print(hardpass)

######## hard methode#######


passward_list=[]
for lr in range(1,nr_letters+1):
    passward_list.append(random.choice(letters))
    print(passward_list)

for sy in range(1,nr_symbols+1):
    passward_list+=random.choice(symbols)
    print(passward_list)
for nu in range(1,nr_numbers):
    passward_list+=random.choice(numbers)
    print(passward_list)
print(f'Your passward is : {passward_list}')

random.shuffle(passward_list)
hardpwd=''
for chr in passward_list:
    hardpwd+=chr

print(f'Your strong passward is: {hardpwd}')