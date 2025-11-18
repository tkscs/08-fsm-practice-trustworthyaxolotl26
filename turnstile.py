# write code to implement a turnstile
print()

state = "locked"
print(f"the turnstile is currently {state}")
while state != "w":
    words = input("whould you like to push(p), give a coin(c) or walk away(w):")
    ac = words
    if ac == "p":
        print("locked out")
        ac = words
    elif ac == "c":
        print("coin acceped")
        state = "unlocked"
        print(f"the turnstile is currently {state}")
        going = input("would you like to push (y/n):" )
        if going == "y":
            print("spinning")
            print("you are on the other side")
            state = "locked"
        else:
            print("pointless, but ok.")
        ac = words
    elif ac == "w":
        state = "w"
    else:
        print("typo, try again")
        ac = words

print()