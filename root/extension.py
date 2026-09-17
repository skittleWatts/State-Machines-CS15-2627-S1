#This is a program for an avid reader.
state = "reading fantasy"

while True:
    if state == "reading fantasy":
        print("You are reading fantasy!")
        while True:
            feeling = input("How are you feeling? ").lower()

            if feeling == "intellectually bored":
                state = "reading non-fiction"
                break
            elif feeling == "in need of a change up":
                state = "reading classics"
                break
            elif feeling == "in need of the goat":
                state = "reading Brandon Sanderson"
                break
            else:
                print("Please enter a valid feeling.")

    elif state == "reading non-fiction":
        print("You are reading non-fiction!")
        while True:
            feeling = input("How are you feeling? ").lower()

            if feeling == "bored":
                state = "reading fantasy"
                break
            elif feeling == "in need of a change up":
                state = "reading classics"
                break
            elif feeling == "in need of the goat":
                state = "reading Brandon Sanderson"
                break
            else:
                print("Please enter a valid feeling.")

    elif state == "reading classics":
        print("You are reading classics!")
        while True:
            feeling = input("How are you feeling? ").lower()

            if feeling == "bored":
                state = "reading fantasy"
                break
            elif feeling == "intellectually bored":
                state = "reading non-fiction"
                break
            elif feeling == "in need of the goat":
                state = "reading Brandon Sanderson"
                break
            else:
                print("Please enter a valid feeling.")

    elif state == "reading Brandon Sanderson":
        print("You are reading Brandon Sanderson!")
        while True:
            feeling = input("How are you feeling? ").lower()

            if feeling == "in need of a change up":
                state = "reading fantasy"
                break
            elif feeling == "intellectually bored":
                state = "reading non-fiction"
                break
            elif feeling == "in need of an older change up":
                state = "reading classics"
                break
            else:
                print("Please enter a valid feeling.")