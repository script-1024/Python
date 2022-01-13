print("What's your name ?")
name=input("> ")
print(f"Nice to meet you, {name} !")
respond = input("> ")
match respond:
    case "Me too" | "Nice to meet you, too":
        print(":)")