# Write your code here :-)
age = 0
print("What is your name?")
name = input()
while age == 0:
    print("Hello " + name + ". How old are you?")
    age = int(input())
    if age >= 130:
        timelord_dict={"Timelord","timelord","Time Lord", "time lord"}
        vampire_dict={"Vampire", "Vampyre", "vampire", "vampyre"}
        print("Are you a timelord, or a vampire?")
        timelord_or_vamp = input()
        if timelord_or_vamp in timelord_dict:
            print("Can I see inside your TARDIS?")
        elif timelord_or_vamp in vampire_dict:
            print("Stay back, I've eaten garlic!")
        else:
            print("Ah, so you are malfunctioning AI.")
    elif age > 40:
        print("Never too old to learn Python!")
    elif age in range(13, 20):
        print("Ah, the joys of youth!")
    else:
        print("Ah, so you are " + str(age) + " years old!")
