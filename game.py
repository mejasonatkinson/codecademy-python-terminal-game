import random
import time
import threading
import os

# Points total
points = 0

# Words total
words = 0

# Characters
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Generate 12 random numbers between 0 and the length of characters using 'random'
list_numbers = [random.randint(0, len(characters) - 1) for _ in range(12)]

# Selectable Characters
list_characters = [characters[n] for n in list_numbers]

# Print list of random characters to screen
print("Initial characters: ", list_characters)

# Timer variable
time_remaining = 60
timer_running = True

def timer():
    global time_remaining, timer_running
    while time_remaining > 0 and timer_running:
        # using 'time'
        time.sleep(1)
        time_remaining -= 1
    if time_remaining <= 0:
        print("\nTime's up!")
        print("Points: ", points)
        print("Words: ", words)
        timer_running = False
        # using 'os' to exit
        os._exit(1)

# Function to validate that the letters in the word are contained in the list_characters variable
def validate(word):
    # TODO - make sure that the character isn't being used multiple times.
    # TODO - make sure that the word is a real word.
    # TODO - make it so that you must have atleast a 3 letter word.
    for char in word:
        if char not in list_characters:
            return False
    return True

# Function to remove characters in list_characters
def removeCharacters(word):
    for char in word:
        if char in list_characters:
            list_characters.remove(char)

# Function to add characters in list_characters to maintain 12 characters using 'random'
def addCharacters():
    num = 12 - len(list_characters)
    temp_list_numbers = [random.randint(0, len(characters) - 1) for _ in range(num)]
    for n in temp_list_numbers:
        list_characters.append(characters[n])
    print("Updated characters: ", list_characters)

# Function to add points (requires global statement to modify global points)
def addPoints(word):
    global points
    # TODO - give different letters, different values?
    points += len(word) * 10

# Function to update words count (requires global statement to modify global words)
def updateWords():
    global words
    words += 1

# Function to test the word
def test(word):
    global time_remaining
    if validate(word):
        addPoints(word)
        updateWords()
        removeCharacters(word)
        addCharacters()
        time_remaining += len(word)  # Add 1 second per character in the word
    else:
        print("Invalid word, try again.")
    return input('Guess a word: ')

# Start the timer thread using 'threading'
timer_thread = threading.Thread(target=timer)
timer_thread.start()

word = input('Guess a word: ')

# Main game loop
while timer_running:
    if word:
        word = test(word)

# Ensure the timer thread stops if the game ends early
timer_thread.join()
