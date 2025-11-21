state = "locked"
words = input("whould you like to push(p), give a coin(c) or walk away(w):")
ac = words

def locked():
    print(f"the turnstile is currently {state}")
    ac = words
    if ac == "p":
        locked()
    elif ac == "c":
        unlocked()

def unlocked():
    print("coin acceped")
    state = "unlocked"
    print(f"the turnstile is currently {state}")
    going = input("would you like to push (y/n):" )
    if going == "y":
        print("spinning")
        print("you are on the other side")
        locked()
    else:
        print("waste of money, but ok.")
        locked()

def leave():
    print('bye :(')


