#title
print("Welcome, type 'cont.' to continue, or 'end' to end.")

print(" ")

#input 1
q=str(input("Enter next step... "))
print(q)

print(" ")

#logic 
if q == "cont.":
    w=str(input("Thank You coming with us on the journey, let us get started with your name... "))

    print(" ")

    print("Oh, hello there ", w, "nice to meet you!")

    print(" ")

    print("You can call me Steph...")

    print(" ")

    print("Narrator: Okay so this is your first choice, please choose wisely")

    print(" ")

    a=("(a)Go f**K yourself")
    b=("(b)Where am I?")
    c=("(c)You are you?")
    d=("(d)...")

    print(" ")

    e=str(input("Enter choice ('a, b, c, d')...."))
    print(" ")

    if e == ("a"):
        print("go f**k yourself as well!!!")

        print("---BAD END---")
    elif e == ("b"):
        print("")


elif q == "end":
    print("Ok you have quit the game")
else:
    print("We are as lost as you are!!!")





