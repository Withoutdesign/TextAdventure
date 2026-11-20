from dialogue import *

def getResponse(options):
    while True:
        response = input().lower()

        if response in options:
            return response
        else:
            print("-(Invalid Response)-\n")

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
    response = getResponse(["start", "quit"])

    match response:
        case "start":
            print("\n>Start<")
            valid = True

            print("It’s 9:30 at night, and the city is still blaring with noise.")
            print("Your clothes haven’t made it into the washer, the garbage is overflowing, and the bathroom sink has been leaking,")
            print("but that's tomorrow's problem, because today's solution is to rot on the couch alongside your brother.")
        
            print("\n*Living the dream*")
            print(">Talk")
            print(">Look Around\n")
            
            response = getResponse(["talk", "look around"])
            match response:
                case "talk":
                    talk()

                case "look around":
                    print("\n>Look Around<")
                    print("The TV is on, playing reruns of the same brain-numbing cartoons you and your brother grew up on.")
                    print("You glance over at him, only to find out that he isn’t even paying attention.")

                    print("\n*I guess reheated food doesn’t taste the same.*")
                    print(">Talk")
                    print(">Leave\n")

                    response = getResponse(["talk", "leave"])
                    match response:
                        case "talk":
                            talk()

                        case "leave":
                            print("\nYou decide to take the party elsewhere, which is to the...")
                            print(">Kitchen")
                            print(">Balcony")
                            print(">Bedroom\n")

                            response = getResponse(["kitchen", "balcony", "bedroom"])
                            match response:
                                case "kitchen":
                                    break
                                case "balcony":
                                    break
                                case "bedroom":
                                    break

        case "quit":
            print("\n>Quit<")
            valid = True
            quit()