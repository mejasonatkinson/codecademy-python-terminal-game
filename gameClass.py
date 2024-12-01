import random
import time
import threading
import os

class WordGame:
    def __init__(self):
        self.points = 0
        self.words = 0
        self.characters = list('abcdefghijklmnopqrstuvwxyz')
        self.list_characters = self.generate_initial_characters()
        self.time_remaining = 60
        self.timer_running = True

    def generate_initial_characters(self):
        list_numbers = [random.randint(0, len(self.characters) - 1) for _ in range(12)]
        return [self.characters[n] for n in list_numbers]

    def start_timer(self):
        timer_thread = threading.Thread(target=self.timer)
        timer_thread.start()
        return timer_thread

    def timer(self):
        while self.time_remaining > 0 and self.timer_running:
            time.sleep(1)
            self.time_remaining -= 1
        if self.time_remaining <= 0:
            self.end_game()

    def end_game(self):
        print("\nTime's up!")
        print("Points: ", self.points)
        print("Words: ", self.words)
        self.timer_running = False
        os._exit(1)

    def validate_word(self, word):
        if len(word) < 3:
            return False
        temp_characters = self.list_characters.copy()
        for char in word:
            if char in temp_characters:
                temp_characters.remove(char)
            else:
                return False
        return True

    def remove_characters(self, word):
        for char in word:
            if char in self.list_characters:
                self.list_characters.remove(char)

    def add_characters(self):
        num = 12 - len(self.list_characters)
        temp_list_numbers = [random.randint(0, len(self.characters) - 1) for _ in range(num)]
        for n in temp_list_numbers:
            self.list_characters.append(self.characters[n])
        print("Updated characters: ", self.list_characters)

    def add_points(self, word):
        self.points += len(word) * 10

    def update_words(self):
        self.words += 1

    def process_word(self, word):
        if self.validate_word(word):
            self.add_points(word)
            self.update_words()
            self.remove_characters(word)
            self.add_characters()
            self.time_remaining += len(word)
        else:
            print("Invalid word, try again.")

    def play(self):
        print("Initial characters: ", self.list_characters)
        timer_thread = self.start_timer()
        word = input('Guess a word: ')

        while self.timer_running:
            if word:
                self.process_word(word)
                if self.timer_running:
                    word = input('Guess a word: ')

        timer_thread.join()

# Create an instance of the WordGame class and start the game
if __name__ == "__main__":
    game = WordGame()
    game.play()
