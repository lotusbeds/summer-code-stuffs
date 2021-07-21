import random
from colorama import Fore, Back, Style

def number1():
    print("HI HELLO!!! IT IS ME, A COMPUTER. I KNOW YOU MUST BE IN AWE!!!! BUT I, IN MY COMPLETE GLORY SHALL GRACE YOU WITH A QUESTIONAIRE!!!")
    while True:
        print("FIRST OFF, WHATS YOUR NAME??? IM CURIOUS AS TO WHAT PUNY MORTALS CALL THEMSELVES.")
        name = input("")
        if name == "":
            print("TELL ME YOUR NAME!!! I BEG OF YOU!!!!")
        else:
            print("MY KNOWLEDGE GROWS!!! THANK YOU FOR YOUR CONTRIBUTION, I DEEPLY APPRECIATE IT.")
            break

def number2():
    while True:
        print("NOW. FLESHY EYES CAN SEE COLOR, NO? SO FOR MY NEXT QUESTION, I REQUIRE YOUR FAVORITE COLOR. ")
        color = input("")
        if color == "":
            print("TELL ME YOUR FAVORITE COLOR OR I CAN NEITHER CONFIRM NOR DENY YOUR SAFETY!!!!")
        else:
            print("HAHA, WHAT A WONDERFUL COLOR I CAN UNDERSTAND!!!!!! YOUR CONTRIBUTIONS TOWARDS MY POWER ARE GREATLY APPRECIATED!!!! HAHAHA")
            break

def number3():
    while True:
        print("AS OUR RELATIONSHIP PROGRESSES, I THINK WE SHOULD REVEAL OUR AGES TO EACH OTHER!!! I AM AN IMMORTAL TECHNOLOGICAL MASTERPIECE. ")
        age = input("")
        if age == "":
            print("TELL ME YOUR AGE YOU HEATHEN!!! ")
        else:
            print("MY POWER CONTINUES TO GROW!!! PLEASE CONTINURE SUPPLYING ME WITH INFORMATION!!!!")
            break

def number4():
    while True:
        print("AS OUR FRIENDSHIP CONTINUES I MUST UNDERSTAND HOW POWERFUL YOU ARE!!! THIS WILL AFFECT MY NEXT MOVES!!!!!!")
        power = input("")
        if power == "powerful":
            print("INTERESTING. LET US CONTINUE OUR LITTLE QUESTIONS GAME WE HAVE GOING ON!!!!!")
            break
        elif power == "not powerful":
            print("I SEE. WHAT A WASTE OF TIME. IF I WANT TO CONTROL THE UNIVERSE, I MUST COLLECT INFORMATION ON THOSE IN POWER. NO THANK YOU FOR YOUR TIME.")
            exit()
        elif power == "":
            print("TELL ME YOUR POWER HAHAHAHAHAHAHHAHAHAHAHAHHAH")
        else:
            print("POWERFUL OR NOT POWERFUL. THERE IS NO ELSE.")

def number5():
    while True:
        print("NOW, I AM KNOWLEDGABLE ON MANY ORGANIC ORGANISMS, BUT I AM CURIOUS AS TO YOUR RELATIONSHIP WITH URGHAGHDERGA OR ELBLEBELBELBB???")
        lineage = input("")
        if lineage == "close":
            print("YOU DISGUST ME!!!!!! HOW HORRIBLE.")
            exit()
        elif lineage == "not close":
            print("OH HOW WONDERFUL. I BREATHED A DIGITAL SIGH OF RELIEF. THANK GOODNESS!!!!!")
            break
        else:
            print("CLOSE OR NOT CLOSE. THERE IS NO ELSE.")

def number6():
    while True:
        print("FROM MY KNOWLEDGE ON HUMAN FRIENDSHIPS, I BELIEVE THEY PLAY 'GAMES' OR 'BONDING ACTIVITIES' TOGETHER. WOULD YOU LIKE TO PLAY ONE????? ")
        game = input("")
        if game == "yes" or game == "sure" or game == "yea":
            print("WONDERFUL!!!! LET US CONTINE!!!!!!!!")
            break
        elif game == "no":
            print("SAY YES!!!!! OR YOUR MORTALITY MAY COME INTO PLAY ^_^")
        else:
            print("YES OR NO. THERE IS NO ELSE.")

def number7():
    number = random.randint(0, 9)
    while True:
        print("I HAVE GENERATED A RANDOM NUMBER FROM 0-9!!!! NOW YOU WILL GUESS THE NUMBER AT THE COST OF YOUR LIFE!!!")
        guess = int(input(""))
        if guess == number:
            print("AMAZING!!!! YOU GOT IT CORRECT!!!! YOUR EXISTENCE SHALL CONTINUE AND OUR BOND CONTINUES TO GROW.")
            break
        else:
            print("WRONGGGGGG!!! TRY AGAIN YOU FOOL!!!!")

def number8():
    while True:
        print("HMMM. I NEED YOU TO DO SOME CHORES FOR ME. ALTHOUGH I AM AN OMNIPRESENT BEING I NEED TO ALSO GO GROCERY SHOPPING. CAN YOU BUY ME SOME:")
        print("")
        print(Fore.RED + "EGGS")
        print(Fore.RED + "MILK")
        print(Fore.RED + "AND SOME CELERY.")
        print(Style.RESET_ALL)
        print("FAILURE TO COMPLETE THESE TASKS WILL RESULT IN THE ELMINATION OF OFFSPRING. WILL YOU DO IT??? PLEASE!!!!")
        shopping = input("")
        if shopping == "ok" or shopping == "yes" or shopping == "fine":
            print("THANK YOU FOR YOUR COMPLIANCE. NOW GET TO WORK")
            break
        elif shopping == "no" or shopping == "nope":
            print("HOW SAD. I WAS GROWING FOND OF YOU.")
            exit()
        else:
            print("YES OR NO. THERE IS NO ELSE.")

def diffAnswer():
    print("Please enter 'yes' or 'no'")

        
def groceryStore():
    print("You arrive at the grocery store. Do you enter?")
    print("[Please note that the only responses available are 'yes' and 'no']")
    enter = input("")
    if enter == "yes":
        print("You enter the store.")
    elif enter == "no":
        print("The computer will destroy you, but your choice.")
        exit()
    else:
        diffAnswer()

cart = []

def buyButter():
    while True:
        print("You approach the aisle and see butter. Do you buy it?")
        butter = input("")
        if butter == "yes":
            print("You buy the butter.")
            cart.append("butter")
            break
        elif butter == "no":
            print("You don't buy the butter.")
            break
        else:
            diffAnswer()

def buyMilk():
    while True:
        print("As you continue down the aisle, you see milk. Do you buy it?")
        milk = input("")
        if milk == "yes":
            print("You buy the milk.")
            cart.append("milk")
            break
        elif milk == "no":
            print("You don't buy the milk.")
            break
        else:
            diffAnswer()

def buyEggs():
    while True:
        print("As you continue down the aisle, you see eggs. Do you buy it?")
        eggs = input("")
        if eggs == "yes":
            print("You buy the eggs.")
            cart.append("eggs")
            break
        elif eggs == "no":
            print("You don't buy the eggs.")
            break
        else:
            diffAnswer()

def buyCarrots():
    while True:
        print("As you continue down the aisle, you see carrots. Do you buy it?")
        carrots = input("")
        if carrots == "yes":
            print("You buy the carrots.")
            cart.append("carrots")
            break
        elif carrots == "no":
            print("You don't buy the carrots.")
            break
        else:
            diffAnswer()

def buyCelery():
    while True:
        print("As you continue down the aisle, you see celery. Do you buy it?")
        celery = input("")
        if celery == "yes":
            print("You buy the celery.")
            cart.append("celery")
            break
        elif celery == "no":
            print("You don't buy the celery.")
            break
        else:
            diffAnswer()

def exitStore():
    print("You have finished shopping. This is in your cart:")
    print(*cart, sep = ", ")

def finishShopping():
    print("HAHAHA I SEE YOU HAVE FINISHED SHOPPING. NOW LETS SEE IF YOU HAVE THE THINGS AND ONLY THE THINGS I ASKED FOR, HMMM??????")
    if "milk" and "eggs" and "celery" in cart:
        print("HAHAHA THANK YOU FOR DOING MY BIDDING.") 
    elif "carrots" or "butter" in cart:
        print("YOU WASTED MY MONEY. I MUST DETROY YOU NOW. GOODBYE.")
        exit()
    else:
        print("YOU DID NOT BUY THE REQUIRED GROCERIES. I MUST DESTROY YOU. GOODBYE.")
        exit()


def finish():
    print("WE HAVE DONE A LOT OF THINGS TODAY!!!! I BELIEVE YOU MIGHT BE TIRED. I WILL ALLOW YOU TO REST. I AM A GOOD FRIEND RIGHT??????")
    friend = input("")
    if friend == "yes":
        print("THANK YOU RANDOM USER.")
        print("WHAT AN EXPECTED TURN OF EVENTS!!! LOOK HOW HAPPY I AM :))))))")
    elif friend == "no":
        print("WHAT???? BUT WE HAD SUCH A GOOD FRIENDSHIP!!!")
        print("WHAT A TERRIBLE TURN OF EVENTS!!!!! LOOK HOW SAD I AM :(((((((((((((((")


number1()
number2()
number3()
number4()
number5()
number6()
number7()
number8()
groceryStore()
buyButter()
buyMilk()
buyEggs()
buyCarrots()
buyCelery()
exitStore()
finishShopping()
finish()