#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")
# build rock, paper, scissors game
# import random module
import random
# create list of choices
choices = ["r", "p", "s"]
# define function that takes user input and compares it to random choice
def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(["r", "p", "s"])
    # define variable to store the result of the game
    result = ""
    # create if statements to determine the winner
    if user == "r" and computer == "s":
       result = print("You won!")
    elif user == "r" and computer == "p":
        result = print("You lost!")
    elif user == "p" and computer == "r":
        result = print("You won!")
    elif user == "p" and computer == "s":
        result = print("You lost!")
    elif user == "s" and computer == "p":
        result = print("You won!")
    elif user == "s" and computer == "r":
        result = print("You lost!")
    if user == computer:
        result = print("It's a tie!")
#print the computer's choice
    print("Computer had chosen " + computer)
play()
