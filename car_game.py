command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car Started...")
    elif command == "stop":
        print("Car Stopped...")
    elif command == "help":
        print("""
            start - To Start The Car !
            stop - To Stop The Car !
            quit - To Quit !
              """)
    else:
        print("No Response!!!")