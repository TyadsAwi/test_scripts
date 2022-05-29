#testing new new code

#this is a dictionary containing {card_digits: [name, pin, amount]}
users = {"1234": ["TJ", "4321", 20000], "5678": ["Tayo", "8765", 30000], "9012": ["Sola", "2109", 15000]}

print("Welcome to T'n'T Cardless ATM")

#this sets a loop that repeats as long as the user's card number is not contained in the list of users
while True:
    card = input("Please input the last 4 digits of your ATM card: ")
    if card not in users.keys():
        print("Invalid card number")
        continue
    else:
        print("Welcome %s" % (users[card][0]))
        break

#this checks the user's pin to be sure it matches the pin attached to teh entered card number before proceeding.
#the first "while" is to repeat the entire ATM sequence if the user decides to perform another transaction.
while True:
    while True:
        pin = input("Please enter your 4 digit pin: ")
        if  users[card][1] == pin:
            print("""Please Select your transaction:
            1 = View Balance
            2 = Transfer
            3 = Withdraw""")
            c = int(input())
            break
        else:
            print("Pin Incorrect!")
            continue

#for account balance check
    if c == 1:
        print("Your Account balaance is %d" %(users[card][2]))

#for transfer
    elif c == 2:
        print("Please enter the amount you wish to transfer:")
        e = input()

        while int(e) > users[card][2]:
            print("Amount entered has exceeded account balance.\n Please enter an amount less than %d" % (users[card][2]))
            e = input()
            continue
        
        print("Please enter the receiver's account number:")
        f = input()
        while len(f) < 10:
            print("Invalid account number. 10 digits required")
            f = input()
            continue
        
        print("""Please select the receiver's bank:
        1 = Access Bank
        2 = Ecobank
        3 = GT Bank
        4 = Kuda Bank
        5 = Zenith Bank""")
        g = input()
        print("Please wait while your transaction is processing")
        print()
        print("Transaction Successful!")
        print("Would you like a receipt for your transaction? Y/N")
        h = input()
        if h == "Y":
            print("Please wait for your receipt")

#for withdrawal
    elif c == 3:
        print("Please select the amount you would like to withdraw:")
        g = input()
        while True:
            if int(g) > (users[card][2]):
                print("Maximum transaction amount exceeded.\n Please enter an amount less than %d" % (users[card][2]))
                g = input ()
                continue
            else:
                print("Please wait while your transaction is processing")
                print()
                print("Transaction Successful!")
                break
            
        print("Would you like a receipt for your transaction? Y/N")
        i = input()
        if i == "Y":
            print("Please wait for your receipt")

    j = input("""Would you like to perform another transaction? Y/N """)

    if j == "Y":
        continue
    if j == "N":
        print("Thank you for banking with us.")
        break

#Also while loop that runs from the very beginning could be added so that when the current user ends the current session, it resets to the beginning to accept another user card input.
