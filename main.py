def title():
    print(".-------------------------.")
    print("|   .---.                 |")
    print("|       | o               |")
    print("|       | .  .--. -. ,-   |")
    print("|       ; |  |  |   :     |")
    print("|   `--'-' `-'  `--' `-   |")
    print("'-------------------------'")
    print(">Start")
    print(">Quit\n")

title()

valid = False

while valid == False:
    response = input()
    response = response.lower() 

    match response:
        case "start":
            print("\n>Start<")
            valid = True
            print("...")

        case "quit":
            print("\n>Quit<")
            valid = True
            quit()
        case _:
            print("-Invalid Response-\n")