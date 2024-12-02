# Terminal Gaming! (wordflow)

I have been addicted to word games for a couple of years now, ever since Wordle sprung into the world. One of the many people who I follow online, Mewtru, decided to make her own version called Wordflow, which works a bit differently but I was hooked as soon as I tried it.

The game is simple.

You have a list of 12 letters and 60 seconds to spell as many words as you can. As you spell the words, you earn points, but more importantly, you earn extra seconds.

At the end of the game, your points and the number of words you entered will be displayed on the screen.

The challenge is to beat your own personal best!

```bash
user@user path % python3 game.py     
Initial characters:  ['r', 'h', 'q', 'r', 'k', 'u', 'b', 'k', 'n', 'g', 'o', 'p']
Guess a word: run
Updated characters:  ['h', 'q', 'r', 'k', 'b', 'k', 'g', 'o', 'p', 'c', 'j', 'f']
Guess a word: 
Time's up!
Points:  30
Words:  1
user@user path %
```

To explain it in a bit more detail about how I got this to work: It required importing a number of packages, most of which I had not used before.

`random` is imported to create random numbers, for picking the letters at the start and when new letters need to be picked.

`time` and `threading` are imported to keep track of the time, which is something I have not done before in Python.

`os` is imported to help exit out of the program when the game runs out of time. It took me a while to figure this out, as a lot of feedback pointed me to using `quit()` or `exit()` without importing the `os` package, and it simply didn't seem to want to work. I finally found the correct solution on trusty Stack Overflow.

I start the program by setting the variables for `points` and `words` to `0`, as well as creating a list of all the characters in the alphabet. I originally did this manually, but then I learned about `list()`, which allows a string to be converted into a list.

For the characters list, I created another list of `12` random numbers from `0` to the length of the characters list, which is then used to set the `12` random characters from the characters.

Printing the initial characters to the screen.

For the timing, I created two variables, `time_remaining`, which I set to `60`, and `timer_running`, which I set to `True`. Then I created a function called `timer`, which pulls in the two set global variables and, using a while loop, checks to see if `time_remaining` is more than `0` and `timer_running` is `True`. If both are true, the program uses the `time` package imported to sleep for 1 second and then removes `1` from the value of `time_remaining`. This repeats until the condition no longer passes. The second half of the function checks to see if `time_remaining` is less than or equal to `0` and prints out a quick message, the points, the words total, sets timer_running to False, and uses the `os` package imported to exit out of the program.

In recapping this, I can see a possible small improvement in removing `timer_running`, but at the same time, using it does make the code more readable.

The `timer` function is called closer to the bottom of the script, using the `threading` package imported to start the `timer` function running while at the same time allowing the rest of the script to run.

The rest of the code mostly relates to testing the input from the player using the inbuilt `input()` function.

While `timer_running` is `True`, and if `input` is `True`, then the script runs the `test` function on the word.

The `test` function takes one parameter: the `word`, running multiple smaller functions.

The first function it runs is to check if the word is valid. `validate` checks if the word is at least `3` characters long; else it returns `False`. It also creates a copy of the characters list, and for each character in the word, checks to see if the character is in the copy of the characters list and removes the character. This prevents the user from being able to use the same character multiple times within one word. If they do, then it returns `False`. If all this passes, the function returns `True`.

There still needs to be another validation placed here to check that the word is, in fact, a real word. But I haven't yet managed to figure out how to do this.

If the `test` function receives `False` from the `validate` function, it will print out a small message stating that the word was invalid and to try again.

If the `test` function receives `True` from the validate function, then the script will proceed to run four more functions.

The `addPoints` function updates the `points` variable with the value of the length of the word times `10`.

This could be improved to make different letters different values, but for the time being, I have left it as it stands.

The `updateWords` function adds `1` to the total of the words variable.

The `removeCharacters` function removes the characters from the list of characters.

The `addCharacters` function finds out how many characters are missing from the list of characters, creates a new temp list of numbers the same length, and adds the new characters to the list, printing out the new updated list.

The `time_remaining` is then updated to equal the current `time_remaining` plus the length of the word guessed.

No matter whether validate returns `True` or `False`, the `test` function returns another `input`, asking the player to Guess a word.

If you want to check out the code for the project, I am hosting it on GitHub here: https://github.com/mejasonatkinson/codecademy-python-terminal-game

I also refactored the code to work as a class.

Overall, this was a fun little project taking me a couple of hours spaced over 3-4 days. I have to admit, I did get stuck in some places and I still think what I have done can be improved. But I am happy with the outcome.

On the topic of what I've learned, I feel a little bit like an imposter. As much as I wanted to code it all from what I had practiced, it just wasn't possible as I had no idea about 3 out of the 4 packages I used. I did figure out most, if not all, of the steps I needed to take on my own but then relied on AI to fill in the missing gaps. I then tried to take the time to learn and understand what the AI had told me, which I hope has stuck with me.

One small thing which annoys me with AI, similar to an over-the-top smart ass at school, is that they just can't help but tell you the answer and won't give you the means to figure it out on your own.