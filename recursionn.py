current_state = "black"

def black():
    print("light is off")
    current_input = input("You can click press (c), hold press (h), or do nothing (n) or put it away (p). Which one do you want? ")
    if current_state == "black":
        # handle each input
        if current_input == "c":
            white()
        elif current_input == "h":
            red()
        elif current_input == "n":
            black()
        elif current_input == "p":
            in_drawer()
        else:
            print(f"Error! I don't recognize the input {current_input}")
            black()

def white():
    print("white light is on")
    current_input = input("You can click press (c), hold press (h), or do nothing (n) or put it away (p). Which one do you want? ")
    if current_state == "black":
        # handle each input
        if current_input == "c":
            white()
        elif current_input == "h":
            red()
        elif current_input == "n":
            black()
        elif current_input == "p":
            in_drawer()
        else:
            print(f"Error! I don't recognize the input {current_input}")
            white()

def red():
    print("red light is on")
    current_input = input("You can click press (c), hold press (h), or do nothing (n) or put it away (p). Which one do you want? ")
    if current_state == "black":
        # handle each input
        if current_input == "c":
            white()
        elif current_input == "h":
            red()
        elif current_input == "n":
            black()
        elif current_input == "p":
            in_drawer()
        else:
            print(f"Error! I don't recognize the input {current_input}")
            red()

def in_drawer():
    print("ded")

black()