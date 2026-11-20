from game import *

def getResponse(options):
    while True:
        response = input().lower()

        if response in options:
            return response
        else:
            print("-(Invalid Response)-\n")

def talk():
    print("\n>Talk<")
    print("<You> What's up?\n")

    print("<Brother> What are you doing?\n")
    print("<You> What do you mean what am I doing?")
    print("<You> I'm trying to talk to my donkey brother.\n")

    print("<Brother> Oh...!")
    print("<Brother> About what...?")
    print(">School")
    print(">Work")
    print(">Life\n")

    response = getResponse(["school", "work", "life"])
    match response:
        case "school" | "work" | "life":
            print("\n<" + response.capitalize() + ">")
            print("<Brother> Yeah, that was a trick question.")
            print("<Brother> I don’t want to talk about that boring crap.")

            print("\nYour brother is known for closing off his emotions, but he is your brother.")
            print("Pushing through the urge to stop talking to him, you give him a face that says it all.\n")

            print("<You> >:(")

            print("\nHe laughs and gets up.\n")

            print("<Brother> Okay...Okay...")
            print("<Brother> If you can guess the number I’m thinking of, we can talk about anything you want.\n")

            print("<Brother> Deal...?")
            print(">Bring it on\n")

            response = getResponse(["bring it on"])
            match response:
                    case "bring it on":
                      print("\n<Bring it on>")
                      game()

                      print(f"\n<You> & <Brother> {randomNumber}")

                      print("\n<Brother> JINX!")
                      