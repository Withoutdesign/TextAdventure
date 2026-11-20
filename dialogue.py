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

    print("<Brother> Oh...")
    print("<Brother> About what...?")
    print(">School")
    print(">Work")
    print(">Life\n")

    response = getResponse(["school", "work", "life"])

    match response:
        case "school" | "work" | "life":
            print("<Brother> Yeah, that was a trick question.")