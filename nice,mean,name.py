#
# Python 3.10.6
#
#Author: Alexis Folse
#
#Purpose: The Tec Academy -Python COurse ,Creating our first program  together.
#         Demonstrating how to pass calible from dunction to function
#         While producing a functional game.
#
#         Rememeber, function_name(variable) _means that we pass in the variable.
#         return variable_means that we are returning the cariable to
#         back to the call function

from turtle import *
import turtle
from turtle import Screen, Turtle

color = (0.60160, 0, 0.99999)  
target = (0.86330, 0.47660, 0.31255)  
turtle.title("Python Guides")
tur = Screen()
tur.tracer(False)

width, height = tur.window_width(), tur.window_height()

deltas = [(hue - color[index]) / height for index, hue in enumerate(target)]

turt = Turtle()
turt.color(color)

turt.penup()
turt.goto(-width/2, height/2)
turt.pendown()

direct = 1

for distance, y in enumerate(range(height//2, -height//2, -1)):

    turt.forward(width * direct)
    turt.color([color[i] + delta * distance for i, delta in enumerate(deltas)])
    turt.sety(y)

    direct *= -1

tur.tracer(True)

def start(nice = 0, mean = 0, name = ""):
    # get user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)

def describe_game(name):
    """
        Check if this is a new game or not.
        If it is new, get the user;s name.
        If it is not a new game, thank the player for
        playing again and continue with the game.
    """
    #meaning, if we do not already have this users name
    #then they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greated \nby several different peopel. \n YOu can chose to be nice or mean.")
                    print(" but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

    
def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (n/m)\n>>>").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice+1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares ar you \nmeanacingly and storm off...")
            mean = (mean+1)
            stop = False
    score(nice, mean, name) #pass the 3 variables to the score()

def show_score(nice, mean, name):
    print( "\n{}, your current total: \n{}, Nice) and({}, mean)".format(name, nice, mean))

def score(nice, mean, name):
     #score function is being passed the values stored within the 3 variables
    if nice > 2 : #"if condition is valid, called win function passing in the variables so it can use them"
        win(nice, mean, name)
    if mean > 2: #"if condition is valid, called win function passing in the variables so it can use them"
        lose(nice, mean, name)
    else:     #else, call nice_mean function passing in the variables so id can use them
        nice_mean(nice, mean, name)



def win(nice, mean, name):
    # Substitute the {} wildcards with out variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of freinds along the way!".format(name))
    # call again funtion and pass in out cariables
    again(nice, mean, name) 


def lose (nice, mean, name):
    #Substitute the {} wildcards with out variable values
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    # call again function and pass in out variables
    again(nice, mean, name)

def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again?(y/n)\n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print ("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter (Y) for 'Yes'; (N) for 'No',\n>>> ")

def reset(nice, mean, name):
    nice = 0
    mean = 0
    #Notice, I do not reset the name variable as that same user has elected to play again
    start(nice, mean, name)




if __name__ == "__main__":
    start()
