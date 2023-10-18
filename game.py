
import random

repeat = True

while repeat:
    number = random.randint(1, 100)
    guess = 0
    tries = 0

while guess != number:
    if  guess < number:
        print("vairāk:")
    else:
        print("mazāk:")

    guess = int(input("uzmini skaitli:"))
    tries += 1
else:
    print(f"Tu uzminēji pēc {tries} reizēm")
if tries < 4 :
    print("tev ļoti labi sanāk")
else:
    print("tev galīgi nesanāk iemācies spēlēt")

    response = input("vai gribi turpināt? y/n")
    if response == "y":
        repeat = True
    elif response == "n":
        repeat = False
        print("Paldies par spēli!  Bye, bye!")
    else:  
        repeat = False
        print("Paldies par spēli!  Bye, bye!")
