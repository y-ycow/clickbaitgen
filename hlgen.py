#Shawn Slaughter
#7-16-24
#Headline

#Init
import random as r
def hl1():
    job = input("enter a job profession(singular)")
    lost = input("enter something that can be lost")
    return("The reason  "+ job + "s are losing their " + lost)

def hl2():
    name = input("enter a last name")
    imp = input("enter something that can be imporved")
    return("These are Dr." + name + "'s 5 ways to improve your "+ imp)

def hl3():
    country = input("enter a country")
    animal = input("enter an animal")
    return("The true reason why "+ animal  + "s are dissapearing in " + country)

def hl4():
    noun = input("enter a noun")
    verb = input("enter a verb")
    return("The real reason your " + noun + verb + "s every day")

def hl5():
    month = input("enter a number between 1 and 12")
    day = input("enter a number between 1 and 30")
    year = input("enter a 4 digit number")
    date = (month + "/" + day + "/" + year)
    return("The reason why " + date + " is the most important date for all of humaninty")

def hl_gen():
    hl = input(" pick a head line(1-5)")
    if hl == "1":
        print(hl1())
    elif hl == "2":
        print(hl2())
    elif hl == "3":
        print(hl3())
    elif hl == "4":
        print(hl4())
    else:
        print(hl5())


hl_gen()
