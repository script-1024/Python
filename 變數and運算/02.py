print("What's your name ?")
print("> ", end="")
name=input()
print(f"Nice to meet you, {name} !")
print("> ", end="")
match input():
    case "Me too":
        print(":)")