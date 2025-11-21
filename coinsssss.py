pockets = []
print("hello and welcome to _ where today you are going broke!!!!!")
print(f"you have {pockets} as of right now, but lets change that!!")
words = ("would yooouuu like tooooo... insert a coin(c), take 1(t1), take 2(t2), or kill the mashine(k): ")
action = ""

def none():
    global words
    global action
    action = input(words)
    if action == "c":
        one()
    elif action == "t1":
        print("no coins")
        none()
    elif action == "t2":
        print("no coins")
        none()
    elif action == "k":
        dead()
    else:
        none()

def one():
    print("there are now one (1) coin(s) in the mashine >:)")
    global action
    action = input(words)
    if action == "c":
        two()
    elif action == "t1":
        poor_options()
        none()
    elif action == "t2":
        print("not enough coins")
        one()
    elif action == "k":
        dead()
    else:
        one()

def two():
    print("there are now two (2) coin(s) in the mashine. >:)")
    global action
    action = input(words)
    if action == "c":
        print("im full")
        two()
    elif action == "t1":
        poor_options()
        one()
    elif action == "t2":
        rich_options()
        none()
    elif action == "k":
        dead()
    else:
        two()

def dead():
    print("noooooo... :(")

def poor_options():
    want = input("your options arrrrree: A FOX! (fox), A CAT! (cat), orrrrrr AN OTTER!! (otter)")
    if want == "fox" or want == "cat" or want == "otter":
        pockets.append(want)
        print(f"you bought a {want}! you now have {pockets}")
    else:
        print("NOT AN OPTION! >:(, try again!!!")
        poor_options()

def rich_options():
    want = input("your options arrrrree: a SHINY fox! (shiny fox), a SHINY cat! (shiny cat), orrrrrr a SHINY otter!! (shiny otter)")
    if want == "shiny fox" or want == "shiny cat" or want == "shiny otter":
        pockets.append(want)
        print(f"you bought a {want}! you now have {pockets}")
    else:
        print("NOT AN OPTION! >:(, try again!!!")
        rich_options()

none()